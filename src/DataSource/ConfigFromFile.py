from src.DataSource.Config import Config
from src.DataSource.RockConstants import RockConstants
import os

class ConfigFromFile(Config):

    def fix_working_directory(self):
        current_working_directory = os.getcwd()
        while "test" in current_working_directory or "src" in current_working_directory:
            os.chdir("../")
            current_working_directory = os.getcwd()

    def get_config(self):
        self.fix_working_directory()
        config_path = RockConstants.file_prefix + "Config/properties.cfg"
        property_file = open(config_path, "r")
        property_data = property_file.read().splitlines()
        property_file.close()
        return property_data
