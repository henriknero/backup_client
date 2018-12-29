import os, pickle
obj_folder = os.path.join(os.path.expanduser('~'), '.gibc')

def save_obj(obj, name):
    if not os.path.exists(obj_folder):
        os.makedirs(obj_folder)
    with open(obj_folder + '/'+ name + '.pkl', 'wb') as file:
        pickle.dump(obj, file, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open(obj_folder + '/' + name + '.pkl', 'rb') as file:
        return pickle.load(file)