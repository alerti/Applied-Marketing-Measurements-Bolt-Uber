import logging
import os
from pathlib import Path

import os
import fnmatch


class Config:
    rt_dir = '/Volumes/Data/'  # root directory
    fil_name = 'Test Task - Marketing Measurement - DF.csv'

    def __init__(self):

        self.logger = logging.getLogger(__name__)
        self.logger.info('Config class created')
        self.logger.info('Config class created')
        self.logger.info('Project directory: {}')
        self.logger.info('Loading .env file')

    def get_data_path(self, root_dir=rt_dir, filename=fil_name):
        link = ''
        for root, dirs, files in os.walk(root_dir):
            for file in files:
                if fnmatch.fnmatch(file, filename):
                    link = os.path.join(root, file)
        return link

    def get_project_dir(self):
        """ Get project directory
        """
        self.logger.info('Getting project directory')
        return self.PROJECT_DIR

    def get_env(self):
        """ Get environment variables
        """
        self.logger.info('Getting environment variables')
        return os.environ

    def set_env(self, key, value):
        """ Set environment variable
        """
        self.logger.info('Setting environment variable')
        os.environ[key] = value
        return None

    def get_env_var(self, key):
        """ Get environment variable
        """
        self.logger.info('Getting environment variable')
        return os.environ[key]

    def get_logger(self):
        """ Get logger
        """
        self.logger.info('Getting logger')
        return self.logger

    def set_logger(self, logger):
        """ Set logger
        """
        self.logger.info('Setting logger')
        self.logger = logger
        return None

    def get_log_fmt(self):
        """ Get log format
        """
        self.logger.info('Getting log format')
        return '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    def get_log_level(self):
        """ Get log level
        """
        self.logger.info('Getting log level')
        return logging.INFO

    def get_log_format(self):
        """ Get log format
        """
        self.logger.info('Getting log format')
        return self.get_log_fmt()

    def get_log_level(self):
        """ Get log level
        """
        self.logger.info('Getting log level')


Config().get_data_path()

import pandas as pd

data = pd.read_csv(Config().get_data_path())
data.head()

# %%
