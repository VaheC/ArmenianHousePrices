import numpy as np
import pandas as pd

from sklearn.linear_model

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_model

from dataclasses import dataclass
import os
import sys

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:

    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self, train_array, test_array):

        try:
            # paste model training procedure code
            logging.info('Splitting dependent and independent variables for train and test data!!!')
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            models_dict = {}

            model_report = evaluate_model(X_train, y_train, X_test, y_test, models_dict)

            best_model_score = ...
            best_model_name = ...
            best_model = ...

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
        except Exception as e:
            logging.info('')
            raise CustomException(e, sys)
