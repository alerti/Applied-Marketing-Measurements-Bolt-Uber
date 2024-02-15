#%%
import logging
import sys
import numpy as np
import pandas as pd
from src.config.config import Config


class DataFunctions:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.info('DataFunctions class created')

    def read_data(self):
        """ Read data from input_filepath
        """
        datainstance = Config()
        input_filepath = datainstance.get_data_path()
        self.logger.info('Reading data from {}'.format(input_filepath))
        data = pd.read_csv(input_filepath, parse_dates=['date'], index_col='date')
        return data

    def write_data(self, data, output_filepath):
        """ Write data to output_filepath
        """
        self.logger.info('Writing data to {}'.format(output_filepath))
        data.to_csv(output_filepath, index=False)
        return None

    def clean_data(self, data):
        """ Clean data
        """
        self.logger.info('Cleaning data')
        data = data.dropna()
        data.head()
        return data

    def add_features(self, data):
        """ Add features to data
        """
        self.logger.info('Adding features to data')
        data['new_feature'] = np.random.rand(data.shape[0])
        return data

    def remove_features(self, data):
        """ Remove features from data
        """
        self.logger.info('Removing features from data')
        data = data.drop(['old_feature'], axis=1)
        return data

    def engineer_features(self, data):
        """ Engineer features in data
        """
        self.logger.info('Engineering features in data')
        data['engineered_feature'] = data['feature1'] * data['feature2']
        return data

    def test_environment(self):

        REQUIRED_PYTHON = "python3"
        system_major = sys.version_info.major
        if REQUIRED_PYTHON == "python":
            required_major = 2
        elif REQUIRED_PYTHON == "python3":
            required_major = 3
        else:
            raise ValueError("Unrecognized python interpreter: {}".format(
                REQUIRED_PYTHON))

        if system_major != required_major:
            raise TypeError(
                "This project requires Python {}. Found: Python {}".format(
                    required_major, sys.version))
        else:
            print(">>> Development environment passes all tests!")
        return None

    def test_datafunctions(self):

        data = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6]})
        data_functions = DataFunctions()
        data = data_functions.clean_data(data)
        data = data_functions.add_features(data)
        data = data_functions.remove_features(data)
        data = data_functions.engineer_features(data)
        return None

    def test_read_data(self):

        data_functions = DataFunctions()
        data = data_functions.read_data('data/raw/data.csv')
        return None

    def test_write_data(self):

        data = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6]})
        data_functions = DataFunctions()
        data_functions.write_data(data, 'data/processed/data.csv')
        return None

# %%
