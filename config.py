from os.path import expanduser, join
import configparser

home_config = join(expanduser('~'), '.config/gibc/config')

config = configparser.SafeConfigParser()
config.read(('default_config','/opt/gibc/default_config', home_config))
API = config['NET']['API']
ROOT = config['NET']['ROOT']
UPDATE_INTERVAL = int(config['NET']['UPD_INTERVAL']) #Update interval set in minutes

ICON = config['FILE']['ICON']