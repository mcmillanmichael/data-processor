import generic.read_csv as read
import preprocess
import one_hotter as hot
import features as feat

def load(file_name, feature_manager, process_data=True):
    """load and preprocess the data"""

    data = read.get_data(file_name, feature_manager.all_features, feature_manager.date_features)
    
    delete_features_as_per_config(data, feature_manager)

    if process_data == True:
        data = process(data, feature_manager)
    return data


def delete_features_as_per_config(data, feature_manager):
    for deleted_feature in list(feature_manager.deleted_features):
        feature_manager.all_features.remove(deleted_feature)
        data.drop(columns=[deleted_feature], inplace=True)


def process(data, feature_manager):
    # preprocess, and normalize data
    preprocess.process(data, feature_manager)

    # one-hot encode all necessary columns, and get new dataframe
    data = hot.process(data, feature_manager)
    
    # just print out the dataframe for now, checking that the new _S8 and _KQ airline columns exist, and have a value
    #o.print_info(apex_data[['arrival_delay', 'departure_delay', 'departure_airline_S8', 'departure_airline_KQ']].head(3))

    # split dates up into (e.g. day_of_week)
    preprocess.engineer_date_features(data, feature_manager)

    data = preprocess.normalize(data, feature_manager)

    return data

#def remove_features():
