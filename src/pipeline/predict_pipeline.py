import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            print(features.columns)
            data_scaled=preprocessor.transform(features)
            print(features.columns)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)
    
class CustomData:
    def __init__( self,
        Hours_Studied: int, 
        CGPA: float, 
        Extracurricular_Activities: str, 
        Sleep_Hours: int,
        Sample_Question_Papers_Practiced: int):
        
        self.Hours_Studied= Hours_Studied 
        self.CGPA= CGPA
        self.Extracurricular_Activities= Extracurricular_Activities
        self.Sleep_Hours= Sleep_Hours
        self.Sample_Question_Papers_Practiced= Sample_Question_Papers_Practiced
        
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Hours_Studied": [self.Hours_Studied],
                "CGPA": [self.CGPA],
                "Extracurricular_Activities": [self.Extracurricular_Activities],
                "Sleep_Hours": [self.Sleep_Hours],
                "Sample_Question_Papers_Practiced": [self.Sample_Question_Papers_Practiced]
            }

            df = pd.DataFrame(custom_data_input_dict, index=None)
            return df

        except Exception as e:
            raise CustomData(e, sys) 