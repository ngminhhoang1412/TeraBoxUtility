import os
import sys


# NOTE: Global constants
RETRY = 3
LOADING_TIMEOUT = 10
LONG_LOADING_TIMEOUT = 30
STAND_BY_TIMEOUT = 15
TRANSITION_TIMEOUT = 5
SHORT_TIMEOUT = 2
MEDIUM_WAIT = [10, 20]
SHORT_WAIT = [2, 5]
VERY_SHORT_WAIT = [0, 1]
LONG_WAIT = [20, 40]
WIDE_WAIT = [1, 10]
PASTE_PERCENTAGE = 50


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except (Exception, SyntaxError):
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# NOTE: Configuration
CWD = resource_path("")
CONFIG_FOLDER = resource_path("config")
env_location = os.path.join(CONFIG_FOLDER, '.env_test')

TEMP_FOLDER = resource_path("temp")
os.makedirs(TEMP_FOLDER, exist_ok=True)
LOG_FILE = os.path.join(TEMP_FOLDER, 'output.log')
PROFILE_FOLDER = os.path.join(TEMP_FOLDER, 'profiles')
PATCHED_DRIVER = os.path.join(TEMP_FOLDER, 'chromedriver.exe')
