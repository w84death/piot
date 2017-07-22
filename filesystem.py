import os.path
import cPickle as pickle
import config

cfg = config.Config()

class Filesystem:
    def __init__(self):
        if(not os.path.isfile(cfg.get_file('data'))):
            self.save([])

    def save(self, list):
        pickle.dump( list, open(cfg.get_file('data'), 'wb'))

    def load(self):
        return pickle.load( open(cfg.get_file('data'), 'rb'))

    def clear(self):
        pickle.dump( [], open(cfg.get_file('data'), 'wb'))

