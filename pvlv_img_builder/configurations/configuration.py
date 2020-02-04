import configparser as cfg


CONFIG_PATH = 'configs/img_builder.cfg'


parser = cfg.ConfigParser()
try:
    parser.read(CONFIG_PATH)
except Exception as exc:
    print(exc)

# colors
GRAY = parser.get('colors', 'GRAY', fallback=(105, 105, 105))
GRAY_BLUE = parser.get('colors', 'GRAY_BLUE', fallback=(180, 180, 255))
DARK_GRAY = parser.get('colors', 'DARK_GRAY', fallback=(62, 62, 62))
LIGHT_GRAY = parser.get('colors', 'LIGHT_GRAY', fallback=(180, 180, 180))
LIGHT_GRAY2 = parser.get('colors', 'LIGHT_GRAY2', fallback=(230, 230, 230))
WHITE = parser.get('colors', 'WHITE', fallback=(255, 255, 255))
BLACK = parser.get('colors', 'BLACK', fallback=(0, 0, 0))
BLUE = parser.get('colors', 'BLUE', fallback=(0, 0, 255))
RED = parser.get('colors', 'RED', fallback=(255, 0, 0))
GREEN = parser.get('colors', 'GREEN', fallback=(0, 128, 0))

# Colors for print out data
DEFAULT_BACKGROUND_COLOR = DARK_GRAY
DEFAULT_TOP_TITLE_COLOR = LIGHT_GRAY2
DEFAULT_TEXT_COLOR = LIGHT_GRAY
DEFAULT_TOWER_1_COLOR = GRAY
DEFAULT_TOWER_2_COLOR = GRAY_BLUE
DEFAULT_TOWER_3_COLOR = GRAY_BLUE

DEFAULT_LEVEL_COLOR = LIGHT_GRAY2
DEFAULT_TITLE_COLOR = LIGHT_GRAY

DEFAULT_BAR_COLOR = LIGHT_GRAY2
DEFAULT_BACKGROUND_BAR_COLOR = GRAY
DEFAULT_XP_INSIDE_DARK_COLOR = GRAY
DEFAULT_XP_INSIDE_LIGHT_COLOR = LIGHT_GRAY2

DIR_DEFAULT_FONT = 'pvlv_img_builder/fonts/helveticaneue-light.ttf'