import pandas as pd
import pickle

import shap
import numpy as np
import matplotlib.pyplot as plt


def normalize_dataframe(df, columns, norm_columns):
    filename = 'assets/models/241017_MinMaxScaler.sav'
    min_max_scaler = pickle.load(open(filename, 'rb'))

    normalized = pd.DataFrame(min_max_scaler.transform(df[columns]),
                         columns=norm_columns)

    FINAL_data_ML = pd.concat([df, normalized], axis=1)
    return FINAL_data_ML

def get_ICU_ML_Prediction(input_data):
       input_data.index = [0]
       # Rename the columns to proper names and convert text bools to integer bools

       input_data_ML = input_data
       input_data_ML["PRIOR CARDIOMYOPATHY"] = input_data['Prior_Cardiomyopathy'].apply(
              lambda x: 1 if x == "Yes" else 0)
       input_data_ML["CHRONIC KIDNEY DISEASE"] = input_data['Chronic Kidney Disease'].apply(
              lambda x: 1 if x == "Yes" else 0)
       input_data_ML["RAISED CARDIAC ENZYMES"] = input_data['Raised Cardiac Enzymes'].apply(
              lambda x: 1 if x == "Yes" else 0)
       input_data_ML["ANAEMIA"] = input_data['Anaemia'].apply(lambda x: 1 if x == "Yes" else 0)
       input_data_ML["STABLE ANGINA"] = input_data['Stable Angina'].apply(lambda x: 1 if x == "Yes" else 0)
       input_data_ML["Acute coronary Syndrome"] = input_data['Acute Coronary Syndrome'].apply(
              lambda x: 1 if x == "Yes" else 0)
       input_data_ML["ST ELEVATION MYOCARDIAL INFARCTION"] = input_data['STEMI'].apply(lambda x: 1 if x == "Yes" else 0)
       input_data_ML["ATYPICAL CHEST PAIN"] = input_data['Atypical Chest Pain'].apply(lambda x: 1 if x == "Yes" else 0)
       input_data_ML["HEART FAILURE"] = input_data['Heart Failure'].apply(lambda x: 1 if x == "Yes" else 0)
       input_data_ML["HEART FAILURE WITH REDUCED EJECTION FRACTION"] = input_data[
              'Heart Failure with Reduced Ejection Fraction'].apply(lambda x: 1 if x == "Yes" else 0)
       input_data_ML["HEART FAILURE WITH NORMAL EJECTION FRACTION"] = input_data[
              'Heart Failure with Normal Ejection Fraction'].apply(lambda x: 1 if x == "Yes" else 0)
       input_data_ML['Complete Heart Block'] = input_data['Complete Heart Block'].apply(lambda x: 1 if x == "Yes" else 0)
       input_data_ML["ACUTE KIDNEY INJURY"] = input_data['Acute Kidney Injury'].apply(lambda x: 1 if x == "Yes" else 0)
       input_data_ML["Atrial Fibrilation"] = input_data['Atrial Fibrillation'].apply(lambda x: 1 if x == "Yes" else 0)
       input_data_ML["Ventricular Tachycardia"] = input_data['Ventricular Tachycardia'].apply(
              lambda x: 1 if x == "Yes" else 0)
       input_data_ML["CARDIOGENIC SHOCK"] = input_data['Cardiogenic Shock'].apply(lambda x: 1 if x == "Yes" else 0)
       input_data_ML["SHOCK"] = input_data['Shock'].apply(lambda x: 1 if x == "Yes" else 0)
       input_data_ML["AGE"] = input_data['Age']
       input_data_ML["Haemoglobin"] = input_data['HB']
       input_data_ML["TOTAL LEUKOCYTES COUNT"] = input_data['Leukocytes']
       input_data_ML["GLUCOSE"] = input_data['Glucose']
       input_data_ML["UREA"] = input_data['Urea']
       input_data_ML["CREATININE"] = input_data['Creatinine']


       columns = ["AGE", "Haemoglobin", "TOTAL LEUKOCYTES COUNT", "GLUCOSE", "UREA", "CREATININE"]
       norm_columns = ["{}_Norm".format(c) for c in columns]

       normalized = normalize_dataframe(input_data_ML, columns, norm_columns)

       final = normalized[['PRIOR CARDIOMYOPATHY', 'CHRONIC KIDNEY DISEASE',
       'RAISED CARDIAC ENZYMES', 'ANAEMIA', 'STABLE ANGINA',
       'Acute coronary Syndrome', 'ST ELEVATION MYOCARDIAL INFARCTION',
       'ATYPICAL CHEST PAIN', 'HEART FAILURE',
       'HEART FAILURE WITH REDUCED EJECTION FRACTION',
       'HEART FAILURE WITH NORMAL EJECTION FRACTION', 'Complete Heart Block',
       'ACUTE KIDNEY INJURY', 'Atrial Fibrilation', 'Ventricular Tachycardia',
       'CARDIOGENIC SHOCK', 'SHOCK', 'AGE_Norm', 'Haemoglobin_Norm',
       'TOTAL LEUKOCYTES COUNT_Norm', 'GLUCOSE_Norm', 'UREA_Norm',
       'CREATININE_Norm']]


       filename = 'assets/models/241022_RF_Model_ICU.sav'
       loaded_model = pickle.load(open(filename, 'rb'))
       result = loaded_model.predict(final)

       result_prob = loaded_model.predict_proba(final)

       return result[0], result_prob[0][1], final

def age_class(age):
    age_group = 1
    if age <= 18:
        age_group = 1  
    elif age <= 35:
        age_group = 2  
    elif age <= 65:
        age_group = 3  
    else:
        age_group = 4  
    return age_group

def normalize_data_dur(df, columns, norm_columns):
    filepath = 'assets/models/fitted_scaler.pkl'
    with open(filepath, 'rb') as file:
       loaded_scaler = pickle.load(file)
       normalized = pd.DataFrame(loaded_scaler.transform(df[columns]),
                         columns=norm_columns)

       FINAL_data_ML = pd.concat([df, normalized], axis=1)
    return FINAL_data_ML
            
def get_duration_label (input_data):
      
      input_data.index = [0]
      input_data_dur = input_data

      input_data_dur["Coronary Artery Disease"] =  input_data['Coronary Artery Disease'].apply(lambda x: 1 if x == "Yes" else 0)
      input_data_dur["Haemoglobin"] = input_data['HB']
      input_data_dur["TOTAL LEUKOCYTES COUNT"] = input_data['Leukocytes']
      input_data_dur["GLUCOSE"] = input_data['Glucose']
      input_data_dur["UREA"] = input_data['Urea']
      input_data_dur["RAISED CARDIAC ENZYMES"] = input_data['Raised Cardiac Enzymes'].apply(
              lambda x: 1 if x == "Yes" else 0)
      input_data_dur["ANAEMIA"] = input_data['Anaemia'].apply(lambda x: 1 if x == "Yes" else 0)
      input_data_dur["STABLE ANGINA"] = input_data['Stable Angina'].apply(lambda x: 1 if x == "Yes" else 0)
      input_data_dur["Acute coronary Syndrome"] = input_data['Acute Coronary Syndrome'].apply(
              lambda x: 1 if x == "Yes" else 0)
      input_data_dur["ST ELEVATION MYOCARDIAL INFARCTION"] = input_data['STEMI'].apply(lambda x: 1 if x == "Yes" else 0)
      input_data_dur["ATYPICAL CHEST PAIN"] = input_data['Atypical Chest Pain'].apply(lambda x: 1 if x == "Yes" else 0)
      input_data_dur["Complete Heart Block"] = input_data['Complete Heart Block'].apply(lambda x: 1 if x == "Yes" else 0)
      input_data_dur["Sick sinus syndrome"] = input_data['Sick Sinus Syndrome'].apply(lambda x: 1 if x == "Yes" else 0)
      input_data_dur["ACUTE KIDNEY INJURY"] = input_data['Acute Kidney Injury'].apply(lambda x: 1 if x == "Yes" else 0)
      input_data_dur["Cerebrovascular Accident INFRACT"] = input_data['Cerebrovascular Accident INFRACT'].apply(lambda x: 1 if x == "Yes" else 0)
      input_data_dur["Ventricular Tachycardia"] = input_data['Ventricular Tachycardia'].apply(
              lambda x: 1 if x == "Yes" else 0)
      input_data_dur["PAROXYSMAL SUPRA VENTRICULAR TACHYCARDIA"] = input_data['PSVT'].apply(
              lambda x: 1 if x == "Yes" else 0)
      input_data_dur["Urinary tract infection"] = input_data['Urinary tract infection'].apply(lambda x: 1 if x == "Yes" else 0)
      input_data_dur["NEURO CARDIOGENIC SYNCOPE"] = input_data['NEURO CARDIOGENIC SYNCOPE'].apply(lambda x: 1 if x == "Yes" else 0)
      input_data_dur["ORTHOSTATIC"] = input_data['ORTHOSTATIC'].apply(lambda x: 1 if x == "Yes" else 0)
      input_data_dur["INFECTIVE ENDOCARDITIS"] = input_data['INFECTIVE ENDOCARDITIS'].apply(lambda x: 1 if x == "Yes" else 0)
      input_data_dur["Deep venous thrombosis"] = input_data['Deep venous thrombosis'].apply(lambda x: 1 if x == "Yes" else 0)
      input_data_dur["SHOCK"] = input_data['Shock'].apply(lambda x: 1 if x == "Yes" else 0)
      input_data_dur["PULMONARY EMBOLISM"] = input_data['Pulmonary Embolism'].apply(lambda x: 1 if x == "Yes" else 0)
      input_data_dur["CHEST INFECTION"] = input_data['CHEST INFECTION'].apply(lambda x: 1 if x == "Yes" else 0)
      input_data_dur["AgeGroup"] = input_data['Age'].apply(lambda x: age_class(x))

      columns_to_norm = ['TOTAL LEUKOCYTES COUNT','GLUCOSE','UREA','Haemoglobin']
      norm_columns = ["{}_Norm".format(c) for c in columns_to_norm]
      
      normalized = normalize_data_dur(input_data_dur, columns_to_norm, norm_columns)
      print(normalized)

      final = normalized[['Coronary Artery Disease', 'Haemoglobin', 'TOTAL LEUKOCYTES COUNT', 'GLUCOSE', 'UREA', 'RAISED CARDIAC ENZYMES', 'ANAEMIA', 'STABLE ANGINA', 'Acute coronary Syndrome', 'ST ELEVATION MYOCARDIAL INFARCTION', 'ATYPICAL CHEST PAIN', 'Complete Heart Block', 'Sick sinus syndrome', 'ACUTE KIDNEY INJURY', 'Cerebrovascular Accident INFRACT', 'Ventricular Tachycardia', 'PAROXYSMAL SUPRA VENTRICULAR TACHYCARDIA', 'Urinary tract infection', 'NEURO CARDIOGENIC SYNCOPE', 'ORTHOSTATIC', 'INFECTIVE ENDOCARDITIS', 'Deep venous thrombosis', 'SHOCK', 'PULMONARY EMBOLISM', 'CHEST INFECTION', 'AgeGroup']]

      model_path = 'assets/models//fitted_RF_model.pkl'
      with open(model_path, 'rb') as file:
       random_forest_model = pickle.load(file)
       result = random_forest_model.predict(final)
       result_prob = random_forest_model.predict_proba(final)

       return result[0], result_prob[0][1], final

           
           


def get_SHAP_Plot(row, filename):


    model = pickle.load(open(filename, 'rb'))
    # Create a TreeExplainer for the uploaded Random Forest model
    explainer = shap.TreeExplainer(model)
    cols = list(row[0:1].columns)
    new_instance = np.array(row[0:1])

    # Calculate SHAP values for a single instance (e.g., the first instance in the test set)
    shap_values = explainer.shap_values(new_instance)

    # Create the waterfall plot using matplotlib
    fig, ax = plt.subplots(figsize=(10, 5))

    shap.waterfall_plot(shap.Explanation(values=shap_values[1][0],
                                         base_values=explainer.expected_value[1],
                                         data=new_instance[0],
                                         feature_names=cols), show=False)




    return fig