import sys
import generic.json_reader as json_reader
import generic.output as o

class ConfigManager:

    config_file = None
    data_file = None
    output_data_file = None
    __feature_manager = None

    def __init__(self, config_file, feature_manager):
        self.config_file = config_file
        self.__feature_manager = feature_manager
        
        self.read_config()


    def read_config(self):
        config = json_reader.read_file(self.config_file)
        self.read_features_from_config(*config['features'])
        self.read_settings_from_config(config['config'])

    def read_features_from_config(self, *features_config):
        for feature in features_config:
            name = feature['name']
            is_date = False
            one_hot = False
            preprocess = False
            delete = False

            if 'delete' in feature:
                delete = feature['delete']

            if delete == False:
                if 'is_date' in feature:
                    is_date = feature['is_date']

                if 'one_hot' in feature:
                    one_hot = feature['one_hot']

                if 'preprocess' in feature:
                    preprocess = feature['preprocess']

            self.__feature_manager.add_feature(name, is_date, one_hot, preprocess, delete)

    def read_settings_from_config(self, config):
        self.data_file = config['inputfile']
        self.output_data_file = config['outputfile']
        
        if self.data_file == None:
            o.print_error('config.json does not have config.inputfile set.')
            sys.exit()
            
        if self.output_data_file == None:
            o.print_error('config.json does not have config.outputfile set.')