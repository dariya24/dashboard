import pandas as pd
import pickle

from sklearn import preprocessing

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


       filename = 'assets/models/241017_random_forest_ICU.sav'
       loaded_model = pickle.load(open(filename, 'rb'))
       result = loaded_model.predict(final)
       return result[0], final