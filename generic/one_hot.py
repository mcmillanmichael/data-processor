import pandas as pd
import output as o

def process_features(dataframe, *features):
    """one-hot encode each feature that needs encoding, add the new features to the dataframe, and remove the original feature"""
    result = dataframe
    try:
        for feature in features:
            o.print_verbose('  one hotting feature: {}'.format(feature))
            
            one_hotted = pd.get_dummies(dataframe[feature], columns=[feature], prefix=feature)
            
            o.print_verbose('  {} unique features found'.format(one_hotted.shape[1]),
                            '')

            result = pd.concat([result, one_hotted], axis=1)
            result.drop(columns=[feature], inplace=True)
    except Exception as e:
        o.print_error(e)
    return result
