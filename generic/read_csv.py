
import pandas as pd
import output as o

def get_data(file, all_feature_headers, date_features):
    try:
        data = pd.read_csv(file, header=None, names=all_feature_headers, parse_dates=date_features)
        
        o.print_verbose('data shape is ' + str(data.shape),
                        'data is a ' + str(type(data)),
                        '')
        
        o.print_info('data columns are: ',
                     data.columns.values,
                     '')

        return data
    except Exception as e:
        print(e)