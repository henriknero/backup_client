from os.path import expanduser, join, realpath, dirname
import configparser

HOME_CONFIG = join(expanduser('~'), '.config/gibc/config')
REAL_DIR = dirname(realpath(__file__))
DEFAULT_CONFIG = join(REAL_DIR, '../default.conf')

config = configparser.SafeConfigParser()
config.read((DEFAULT_CONFIG, '/opt/gibc/default_config', HOME_CONFIG))

class Config:
    API = config['NET']['API']
    ROOT = config['NET']['ROOT']
    UPDATE_INTERVAL = int(config['NET']['UPD_INTERVAL']) #Update interval set in minutes

    ICON = join(REAL_DIR, 'icon.png')
