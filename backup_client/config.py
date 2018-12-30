from os.path import expanduser, join, realpath, dirname
import configparser

home_config = join(expanduser('~'), '.config/gibc/config')
real_dir = dirname(realpath(__file__))
default_config = join(real_dir, '../default.conf')

config = configparser.SafeConfigParser()
config.read((default_config, '/opt/gibc/default_config', home_config))

class Config:
    API = config['NET']['API']
    ROOT = config['NET']['ROOT']
    UPDATE_INTERVAL = int(config['NET']['UPD_INTERVAL']) #Update interval set in minutes

    ICON = join(real_dir, 'icon.png')

