import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        
    def get_data_transformer_object(self):
        '''
        This method is responsible for data transformation
        '''
        try:
            Num_Col = ['Hours Studied', 'Sleep Hours', 'Sample Question Papers Practiced', 'CGPA']
            Cat_Col = ['Extracurricular Activities']
            
            Num_Pipeline = Pipeline(
                steps=[
                    ('Scalar', StandardScaler(with_mean=False))
                ]
            )
            
            Cat_Pipeline = Pipeline(
                steps=[
                    ('OneHotEncoder', OneHotEncoder()),
                    ('Scalar', StandardScaler(with_mean=False))
                ]
            )
            
            logging.info('Preprocessing done for Categorical Column')
            logging.info('Preprocessing done for Numerical Column')
            
            preprocessor = ColumnTransformer(
                [
                    ('Num_Pipeline',Num_Pipeline,Num_Col),
                    ('Cat_Pipeline',Cat_Pipeline,Cat_Col)
                ]
            )
            
            return preprocessor 
            
        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logging.info('Read train and test data')
            
            logging.info('Obtaining preprocessing object')
            
            preprocessor_obj = self.get_data_transformer_object()
            
            target_column_name = 'Performance Index'
            
            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info("Applying preprocessing object on training dataframe and testing dataframe.")
            
            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessor_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]
            logging.info(f"Saved preprocessing object.")

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_obj

            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
            
        except Exception as e:
            raise CustomException(e, sys)