from os.path import expanduser, join, realpath, dirname
import configparser


HOME_CONFIG = join(expanduser('~'), '.config/gibc/config')
REAL_DIR = dirname(realpath(__file__))
ROOT_DIR = dirname(REAL_DIR)
DEFAULT_CONFIG = join(ROOT_DIR, 'default.conf')

config = configparser.SafeConfigParser()
config.read((DEFAULT_CONFIG, '/opt/gibc/default_config', HOME_CONFIG))

class Config:
    API = config['NET']['API']
    ROOT = config['NET']['ROOT']
    UPDATE_INTERVAL = int(config['NET']['UPD_INTERVAL']) #Update interval set in minutes
