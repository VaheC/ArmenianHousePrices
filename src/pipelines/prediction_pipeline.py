import sys 
import os 

from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

import pandas as pd

class CustomData:
    # get in the data and convert into pandas dataframe

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            model_path = os.path.join('artifacts', 'model.pkl')

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            data_scaled = preprocessor.tranform(features)
            pred = model.predict(data_scaled)
            return pred
        except Exception as e:
            raise CustomException(e, sys)