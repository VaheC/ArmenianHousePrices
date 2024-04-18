import os 
import sys
import pickle
import numpy as np
import pandas as pd

from src.exception import CustomException
from src.logger import logging

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.mkdir(dir_path, exist_ok=True)
        pickle.dump(obj, open(file_path, 'wb'))
    except Exception as e:
        raise CustomException(e, sys)