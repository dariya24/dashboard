import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from collections import defaultdict
import statsmodels.formula.api as smf

#data preprocessing
df = pd.read_csv("data/HDHI_Admission_data_post_processed.csv")
age_group_mapping = {
'<18': 1, '18 - 35': 2,'36 - 65': 3,'>65':4 
}

df_binary = df.drop(['Unnamed: 0','SNO', 'MRD No.', 'D.O.A', 'D.O.D', 'AGE', 'GENDER','RURAL','DURATION OF STAY','duration of intensive unit stay', 'OUTCOME','month year','Haemoglobin','TOTAL LEUKOCYTES COUNT','PLATELETS','GLUCOSE','UREA','CREATININE','B-TYPE NATRIURETIC PEPTIDE','Ejection Fraction'], axis=1)
df_binary.dropna(axis=0, inplace=True)
df_binary['Duration_Label'] = df_binary['Duration_Label'].map({'LT7': 0, 'GE7': 1})
df_binary['AgeGroup']=df_binary['AgeGroup'].map(age_group_mapping)
df_binary['TYPE OF ADMISSION-EMERGENCY/OPD'] = df_binary['TYPE OF ADMISSION-EMERGENCY/OPD'].map({'E': 0, 'O': 1})

df_continue = df[['Duration_Label','boolGender','boolRural', 'AGE', 'Haemoglobin', 'TOTAL LEUKOCYTES COUNT', 'PLATELETS', 'GLUCOSE', 'UREA', 'CREATININE', 'B-TYPE NATRIURETIC PEPTIDE', 'Ejection Fraction','AgeGroup','ICU_admission_status']]
df_continue.dropna(axis=0, inplace=True)
df_continue['AgeGroup']=df_continue['AgeGroup'].map(age_group_mapping)
df_continue['Duration_Label'] = df_continue['Duration_Label'].map({'LT7': 0, 'GE7': 1})

#statmodel buildup
def find_zero_variance_columns(df):
    """Identifies columns in a DataFrame that have zero variance."""
    return [col for col in df.columns if df[col].nunique() == 1]

def logistic_regression_analysis(df, group_col, target_col):
    results_dict = {}
    groups = df[group_col].unique()

    for group in groups:
        #print(f"Processing group: {group}")
        subgroup = df[df[group_col] == group]

        # Identify and remove zero variance columns
        zero_variance_cols = find_zero_variance_columns(subgroup)
        if zero_variance_cols:
            #print(f"Removing zero variance columns for group {group}: {zero_variance_cols}")
            subgroup = subgroup.drop(columns=zero_variance_cols)

        X = subgroup.drop(columns=[target_col])
        if X.empty:
            #print(f"No variables to analyze in subgroup {group}, skipping.")
            continue

        y = subgroup[target_col]
        X_const = sm.add_constant(X, has_constant='add')

        try:
            # First attempt with default method
            logit_model = sm.Logit(y, X_const)
            result = logit_model.fit(disp=0)
        except (np.linalg.LinAlgError, sm.tools.sm_exceptions.PerfectSeparationError):
            #print(f"Singular matrix or perfect separation error in group {group}. Trying regularized logistic regression.")
            try:
                # Use regularized logistic regression as a fallback
                logit_model = sm.Logit(y, X_const)
                # Adjust the regularization method and strength as needed
                result = logit_model.fit_regularized(method='l1', maxiter=100, disp=0)
            except Exception as e:
                #print(f"Regularized logistic regression failed for group {group}: {e}")
                continue

        # Extract p-values and odds ratios if available
        subgroup_results = {}
        if hasattr(result, 'pvalues') and not np.isnan(result.pvalues).all():
            for variable in result.params.index:
                p_value = result.pvalues[variable]
                odds_ratio = np.exp(result.params[variable])
                if p_value < 0.05 and odds_ratio > 1:
                    subgroup_results[variable] = {
                        'p_value': p_value,
                        'odds_ratio': odds_ratio
                    }
        else:
            #print(f"P-values not available for group {group}, computing using robust standard errors.")
            try:
                robust_results = result.get_robustcov_results(cov_type='HC0')
                for variable in robust_results.params.index:
                    p_value = robust_results.pvalues[variable]
                    odds_ratio = np.exp(robust_results.params[variable])
                    if p_value < 0.05 and odds_ratio > 1:
                        subgroup_results[variable] = {
                            'p_value': p_value,
                            'odds_ratio': odds_ratio
                        }
            except Exception as e:
                #print(f"Failed to compute robust standard errors for group {group}: {e}")
                continue

        results_dict[group] = subgroup_results

    return results_dict

#merge dictionaries
def deep_merge(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if isinstance(value, dict):
            # get node or create one
            node = result.setdefault(key, {})
            deep_merge(node, value)
        else:
            result[key] = value
    return result

#process rsik factors in different subpopulation
def process_regression_results(results_dict):
    all_variables = set()
    variable_groups = defaultdict(set)
    processed_results = {
        "shared_risk": defaultdict(dict),
        "unique_risk": {},
        "groups": set(results_dict.keys())  # Keep track of all groups
    }
    
    # Collect all variables and their groups
    for group, variables in results_dict.items():
        if variables:  # Only process if variables exist
            all_variables.update(variables.keys())
            for variable in variables.keys():
                variable_groups[variable].add(group)
        else:
            # If the group has no variables, we still note it
            variable_groups[None].add(group)
    
    # Process shared variables
    for variable, groups in variable_groups.items():
        if variable is None:
            continue  # Skip placeholder for groups with no variables
        if len(groups) > 1:  # Shared by at least 2 groups
            shared_key = f"shared_by_{len(groups)}_groups"
            processed_results["shared_risk"][shared_key][variable] = {
                f'group_{group}_odds_ratio': results_dict[group][variable]['odds_ratio']
                for group in groups
            }
        else:  # Unique to one group
            group = list(groups)[0]
            processed_results["unique_risk"][f'{variable}_group_{group}'] = {
                'odds_ratio': results_dict[group][variable]['odds_ratio']
            }
    
    return processed_results

#create risk factor table
def create_risk_table(processed_results):
    # Initialize an empty dictionary to store all risks
    all_risks = {}

    # Collect all groups from the processed results
    all_groups = processed_results.get('groups', set())
    group_columns = [f'group_{group}_odds_ratio' for group in sorted(all_groups)]

    # Collect all variables from shared and unique risks
    all_variables = set()
    for risks in processed_results['shared_risk'].values():
        all_variables.update(risks.keys())
    all_variables.update(var.split('_group_')[0] for var in processed_results['unique_risk'].keys())

    # Initialize the risk table with NaN for all groups and variables
    for variable in all_variables:
        all_risks[variable] = {col: np.nan for col in group_columns}

    # Update with actual values where available
    # Process shared risks
    for sharing_level, risks in processed_results['shared_risk'].items():
        for variable, group_data in risks.items():
            for group_key, odds_ratio in group_data.items():
                all_risks[variable][group_key] = odds_ratio

    # Process unique risks
    for risk_key, data in processed_results['unique_risk'].items():
        variable, group = risk_key.rsplit('_group_', 1)
        group_key = f'group_{group}_odds_ratio'
        all_risks[variable][group_key] = data['odds_ratio']

    # Create DataFrame from the dictionary
    df = pd.DataFrame.from_dict(all_risks, orient='index', columns=group_columns)

    # Optionally, sort the DataFrame by variable names
    df = df.sort_index()

    return df


st.set_page_config(
    page_title="PRAIS - Diagnostic",
    page_icon="👋",
)

st.sidebar.image("./assets/P R A I S.png",)

st.header("Risk factors")

labs = ["The odd of staying in hosptial longer than 7 days", "The odd of getting admitted to ICU"]

option = st.selectbox(
    "Which target variables do you want to include?",
    labs,
)

subpopulation = st.selectbox(
    "What demographic parameter do you want to include?",
    ["Location", "Gender", "Age group"],
)


if option == "The odd of staying in hosptial longer than 7 days":
    para1 = 'Duration_Label'
elif option == "The odd of getting admitted to ICU":
    para1 = 'ICU_admission_status'

if subpopulation == "Location":
    para2 = 'boolRural'
elif subpopulation == "Gender":
    para2 = 'boolGender'
elif subpopulation == "Age group":
    para2 = 'AgeGroup'


binary_results = logistic_regression_analysis(df_binary, para2, para1)
continue_results = logistic_regression_analysis(df_continue, para2, para1)
combine_result = deep_merge(binary_results,continue_results)
processed_result = process_regression_results(combine_result)
risk_table = create_risk_table(processed_result)

if subpopulation == "Location":
    risk_table.rename(columns={
    'group_0_odds_ratio': 'urban group odds ratio',
    'group_1_odds_ratio': 'rural group odds ratio'
}, inplace=True)
    
elif subpopulation == "Gender":
    risk_table.rename(columns={
    'group_0_odds_ratio': 'female group odds ratio',
    'group_1_odds_ratio': 'male group odds ratio'
}, inplace=True)
    
elif subpopulation == "Age group":
    risk_table.rename(columns={
    'group_1_odds_ratio': '<18 age group odd ratio',
    'group_2_odds_ratio': '18-35 age group odds ratio',
    'group_3_odds_ratio': '36-65 age group odds ratio',
    'group_4_odds_ratio': '>65 age group odds ratio',
}, inplace=True)
variables_to_remove = ["AgeGroup", "boolRural", "boolGender", "ICU_admission_status",'const']
risk_table.drop(labels=variables_to_remove, errors='ignore', inplace=True)
risk_table.fillna(0, inplace=True)

st.bar_chart(risk_table, horizontal= True, stack=False)

#st.dataframe(risk_table)



