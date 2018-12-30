import os
import pickle

OBJ_FOLDER = os.path.join(os.path.expanduser('~'), '.gibc')

def save_obj(obj, name):
    if not os.path.exists(OBJ_FOLDER):
        os.makedirs(OBJ_FOLDER)
    with open(OBJ_FOLDER + '/'+ name + '.pkl', 'wb') as file:
        pickle.dump(obj, file, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open(OBJ_FOLDER + '/' + name + '.pkl', 'rb') as file:
        return pickle.load(file)
