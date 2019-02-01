import pandas as pd
import generic.output as o
import generic.one_hot as hot
import features as feat


def process(apex_data, feature_manager):
    """one-hot-encode the given apex_data"""
    try:

        o.print_info('shape before one_hot: ' + str(apex_data.shape))
        
        # one-hot encode the given features, merge the new features into a new dataframe, and return it.
        apex_data = hot.process_features(apex_data, *feature_manager.one_hot_features)

        o.print_info('shape after one_hot: ' + str(apex_data.shape),
                    '')

        return apex_data

    except Exception as e:
        o.print_error(e)