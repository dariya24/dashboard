import numpy as np
import pandas as pd
import scipy.stats.distributions as dist
from statsmodels.stats.proportion import proportions_ztest

def get_pvalue_propotion(df, var1, var2):
    groups = df[var2].unique()
    groupA = groups[0]
    groupB = groups[1]
    contingency_table = pd.crosstab(df[var1], df[var2]).reset_index()  # Contingency Table
    A00 = int(contingency_table[contingency_table[var1] == 0][groupA])
    A01 = int(contingency_table[contingency_table[var1] == 0][groupB])
    A10 = int(contingency_table[contingency_table[var1] == 1][groupA])
    A11 = int(contingency_table[contingency_table[var1] == 1][groupB])

    print("{}: {}, {}:{}".format(groupA, A00 / (A00 + A10), groupB, A01 / (A01 + A11)))

    count = np.array([A00, A01])
    nobs = np.array([A00 + A10, A01 + A11])
    stat, pval = proportions_ztest(count, nobs)
    if pval < 0.005:
        significant = 1
        text = "Statistically significant, p-value <0.005"
        color = "green"
    else:
        significant = 0
        text = "NOT statistically significant, p-value {0:.3f}".format(pval)
        color = "red"

    return text, color



def prepare_dataframe_for_descriptive_analytics(df):
    df.rename(columns={"AGE": "Age", "GENDER": "Gender", "RURAL": "Rural or Urban", "Duration_Label": "Length of stay"}, inplace=True)

    df.replace("LT7", "Less than 7 days", inplace=True)
    df.replace("GE7", "7 or more days", inplace=True)

    df.replace("F", "Female", inplace=True)
    df.replace("M", "Male", inplace=True)

    df.replace("R", "Rural", inplace=True)
    df.replace("U", "Urban", inplace=True)

    df.rename(
        columns={
            "TOTAL LEUKOCYTES COUNT": "Total Leukocytes Count",
            "PLATELETS": "Platelets",
            "GLUCOSE": "Glucose",
            "UREA,CREATININE": "Urea,Creatinine"
        }, inplace=True
    )


    cols_to_rename = ["SMOKING ", "ALCOHOL", "Diabetes Mellitus", "Hypertension", "Coronary Artery Disease",
    "PRIOR CARDIOMYOPATHY", "CHRONIC KIDNEY DISEASE",
    'SEVERE ANAEMIA', 'ANAEMIA', 'STABLE ANGINA',
    'Acute coronary Syndrome', 'ST ELEVATION MYOCARDIAL INFARCTION',
    'ATYPICAL CHEST PAIN', 'HEART FAILURE',
    'HEART FAILURE WITH REDUCED EJECTION FRACTION',
    'HEART FAILURE WITH NORMAL EJECTION FRACTION', 'Valvular Heart Disease',
    'Complete Heart Block', 'Sick sinus syndrome', 'ACUTE KIDNEY INJURY',
    'Cerebrovascular Accident INFRACT', 'Cerebrovascular Accident BLEED',
    'Atrial Fibrilation', 'Ventricular Tachycardia',
    'PAROXYSMAL SUPRA VENTRICULAR TACHYCARDIA', 'Congenital Heart Disease',
    'Urinary tract infection', 'NEURO CARDIOGENIC SYNCOPE', 'ORTHOSTATIC',
    'INFECTIVE ENDOCARDITIS', 'Deep venous thrombosis', 'CARDIOGENIC SHOCK',
    'SHOCK', 'PULMONARY EMBOLISM', 'CHEST INFECTION']

    new_cols_names = [x.lower().title() for x in cols_to_rename]

    print(new_cols_names)

    dict_cols = {}

    for i in range(len(cols_to_rename)):
        dict_cols[cols_to_rename[i]] = new_cols_names[i]



    df.rename(
        columns=dict_cols, inplace=True
    )



    return df
