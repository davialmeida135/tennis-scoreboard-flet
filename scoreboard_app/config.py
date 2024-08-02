from flet import colors
APP_BG = colors.DEEP_ORANGE_400
BOTTOM_BAR = colors.GREEN
MAIN_COLOR_1 = colors.GREEN_800
MAIN_COLOR_2 = colors.LIGHT_GREEN_900

CURRENT_SET_COLOR_1 = colors.LIGHT_GREEN
CURRENT_SET_COLOR_2 = colors.GREEN

CURRENT_GAME_COLOR_1 = colors.WHITE
CURRENT_GAME_COLOR_2 = colors.GREY_400

SCOREBOARD_TEXT_SIZE = 20
SCOREBOARD_PLAYER_SIZE = 16

# config.py
from flet import colors
import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Application constants
APP_BG = colors.DEEP_ORANGE_400
BOTTOM_BAR = colors.GREEN
MAIN_COLOR_1 = colors.GREEN_800
MAIN_COLOR_2 = colors.LIGHT_GREEN_900

CURRENT_SET_COLOR_1 = colors.LIGHT_GREEN
CURRENT_SET_COLOR_2 = colors.GREEN

CURRENT_GAME_COLOR_1 = colors.WHITE
CURRENT_GAME_COLOR_2 = colors.GREY_400

SCOREBOARD_TEXT_SIZE = 20
SCOREBOARD_PLAYER_SIZE = 16
"""
# Application name and author
app_name = "scoreboard_app"
app_author = "davi_almeida"

# Get the directories for the application
dirs = PlatformDirs(app_name, app_author)

# Log the directories
logging.debug(f"Data directory: {dirs.user_data_dir}")
logging.debug(f"Config directory: {dirs.user_config_dir}")
logging.debug(f"Cache directory: {dirs.user_cache_dir}")

# Use a directory within the app's data storage
keyring_dir = os.path.join(dirs.user_data_dir, ".keyring")

# Ensure the keyring directory exists
if not os.path.exists(keyring_dir):
    try:
        os.makedirs(keyring_dir)
        logging.debug(f"Keyring directory created: {keyring_dir}")
    except PermissionError as e:
        logging.error(f"PermissionError: {e}")
        raise

# Set the keyring backend to use a custom file path
keyring_backend = keyrings.alt.file.PlaintextKeyring()
keyring_backend.file_path = os.path.join(keyring_dir, "keyring_pass.cfg")
keyring.set_keyring(keyring_backend)"""