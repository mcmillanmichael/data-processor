
from sklearn import preprocessing
import pandas as pd
import features as feat
import generic.output as o

# preprocessing essentially does: field.mean / field.std, 
# to bring the values closer to zero, whilst maintaining the differential between values

def process(apex_data, feature_manager):
    """preprocesses the given features"""
    for feature in feature_manager.preprocess_features:
        apex_data[feature] = preprocessing.scale(apex_data[[feature]])

def engineer(data, feature_manager):
    """engineer some features"""
    engineer_date_features(data, feature_manager)

def engineer_date_features(data, feature_manager, drop_original_feature=True):
        
    for feature in feature_manager.date_features:
        # hour_of_day
        o.print_info('transforming {} to {}_hour_of_day'.format(feature, feature))
        data[feature + '_hour_of_day'] = pd.to_numeric(data.apply(lambda row: get_hour_of_day(row, feature), axis=1))

        # day_of_week
        o.print_info('transforming {} to {}_day_of_week'.format(feature, feature))
        data[feature + '_day_of_week'] = pd.to_numeric(data.apply(lambda row: get_day_of_week(row, feature), axis=1))

        # week_of_year
        o.print_info('transforming {} to {}_week_of_year'.format(feature, feature))
        data[feature + '_week_of_year'] = pd.to_numeric(data.apply(lambda row: get_week_of_year(row, feature), axis=1))

        if drop_original_feature == True:
            data.drop(columns=[feature], inplace=True)
        
    o.print_info('datetime feature engineering complete.')

def normalize(data, feature_manager):
    try:
        return preprocessing.normalize(data.columns.values)
    except Exception as ex:
        o.print_error(ex)
    # see C:\Source\data-chapter\iris-classification-tensorflow\iris-classification.py


def get_hour_of_day(row, feature):
    date = row[feature]
    result = date.hour + (date.minute / 60) + (date.second / 3600)
    return result
    
def get_day_of_week(row, feature):
    date = row[feature]
    result = date.dayofweek
    return result
    
def get_week_of_year(row, feature):
    date = row[feature]
    result = date.weekofyear
    return result