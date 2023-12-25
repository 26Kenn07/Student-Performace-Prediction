import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_objecct

class PredictPipeline:
    def __init__(self):
        pass
    
class CustomData:
    def __init__( self,
        Gender: str, 
        Age: int, 
        Occupation: str, 
        Sleep_Duration: float, 
        Quality_of_Sleep: int, 
        Physical_Activity_Level: int, 
        Stress_Level: int,
        BMI_Category: str, 
        Blood_Pressure: str, 
        Heart_Rate: int, 
        Daily_Steps: int):
        
        self.Gender = Gender  
        self.Age = Age 
        self.Occupation = Occupation 
        self.Sleep_Duration = Sleep_Duration
        self.Quality_of_Sleep = Quality_of_Sleep
        self.Physical_Activity_Level = Physical_Activity_Level
        self.Stress_Level = Stress_Level 
        self.BMI_Category = BMI_Category 
        self.Blood_Pressure = Blood_Pressure
        self.Heart_Rate = Heart_Rate
        self.Daily_Steps = Daily_Steps
        