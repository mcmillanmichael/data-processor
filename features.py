
class FeatureManager:

    # all features that are in the csv file, including features we want to delete.
    all_features = []

    # features that are datetimes
    date_features = []

    # features to be one hotted
    one_hot_features = []

    # features to go through preprocessing
    preprocess_features = []

    # features that are in the csv file, but we don't want to process.
    deleted_features = []

    def add_feature(self, name, is_date, one_hot, preprocess, delete):
        """add the given feature to the relevant bins"""
        self.all_features.append(name)
        
        if is_date == True:
            self.date_features.append(name)

        if one_hot == True:
            self.one_hot_features.append(name)
        
        if preprocess == True:
            self.preprocess_features.append(name)
        
        if delete == True:
            self.deleted_features.append(name)