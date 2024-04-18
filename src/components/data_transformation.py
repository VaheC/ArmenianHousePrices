from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

import numpy as np
import pandas as pd

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

import os
import sys
from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def initiate_data_transformation(self):

        try:
            logging.info('Data Transformation initiated!!!')

            # get categorical and numerical columns
            categorical_columns = 
            numerical_columns = 

            # assign categorical rankings if exists

            logging.info("Data Transformation Pipeline initiated!!!")

            # paste pipelines below

            preprocessor = ...

            logging.info("Data Transformation completed!!!")

            return preprocessor
        
        except Exception as e:
            logging.info('Exception occured in Data Transformation!!!')
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_data_path, test_data_path):

        try:
            train_df = pd.read_csv(train_data_path)
            test_df = pd.read_csv(test_data_path)

            logging.info('Train and test data loaded!!!')
            logging.info(f'Train data head : \n{train_df.head().to_string()}')
            logging.info(f'Test data head : \n{test_df.head().to_string()}')

            logging.info('Obtaining preprocessing object!!!')

            preprocessing_obj = self.get_data_transformation_object()

            target_column = 'name of target col'
            drop_columns = [target_column, 'id']

            input_feature_train_df = train_df.drop(columns=drop_columns)
            target_feature_train_df = train_df[target_column]

            input_feature_test_df = test_df.drop(columns=drop_columns)
            target_feature_test_df = test_df[target_column]

            input_feature_train_array = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_array = preprocessing_obj.transform(input_feature_test_df)

            train_array = np.c_[input_feature_train_array,  np.array(target_feature_train_df)]
            test_array = np.c_[input_feature_test_array,  np.array(target_feature_test_df)]

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            logging.info('Preprocesing of train and test data is completed!!!')

            return (
                train_array,
                test_array,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            logging.info("Exception occured preprocessing of train and test data!!!")
            raise CustomException(e, sys)