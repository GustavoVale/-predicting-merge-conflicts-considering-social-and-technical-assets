from sklearn.ensemble import RandomForestClassifier
import utils
from ml_classifiers.metrics_entity import Metrics

class Random_forest:

    def __init__(self, dictionary, data_types, balancing_techniques, algo_mode) -> None:
            self.data_types = data_types
            self.balancing_techniques = balancing_techniques
            self.algo_mode = algo_mode

            self.max_depths = dictionary.get("max_depths", None)
            self.max_features = dictionary.get("max_features", None)
            self.min_samples_leaves = dictionary.get("min_samples_leaves", None)
            self.min_samples_splits = dictionary.get("min_samples_splits", None)
            self.n_estimators = dictionary.get("n_estimators", None)
            self.criteria = dictionary.get("criteria", None)
            self.warm_starts = dictionary.get("warm_starts", None)
            
            self.is_valid_object = self.__is_valid_object()

    def __is_valid_object(self):
        return None not in [self.max_depths, self.max_features, self.min_samples_leaves, self.min_samples_splits, self.n_estimators, self.criteria]

    def run(self):
        print('\nRANDOM FOREST is running\n')

        for data_type in self.data_types:

            path = utils.get_path(data_type)

            for technique in self.balancing_techniques:
                data_train = utils.get_data_train(technique, path)

                y_train, x_train, y_test, x_test = utils.get_x_y_train_and_test_data(data_train, path)

                metrics = Metrics()

                # Hyper-parameters
                for max_depth in self.max_depths:
                    for max_feature in self.max_features:
                        for min_samples_leaf in self.min_samples_leaves:
                            for min_samples_split in self.min_samples_splits:
                                for estimator in self.n_estimators:
                                    for criterion in self.criteria:
                                        for warm_start in self.warm_starts:

                                            hyper_parameters = "max_depth:", max_depth, " max_feature:", max_feature, " min_samples_leaf:", min_samples_leaf, \
                                            " min_samples_split:", min_samples_split, " estimator:", estimator, " criterion:", criterion, " warm_start:", warm_start

                                            model = RandomForestClassifier(n_estimators=estimator, criterion=criterion, min_samples_split=min_samples_split,
                                                                            min_samples_leaf=min_samples_leaf, max_depth=max_depth,
                                                                            max_features=max_feature, warm_start=warm_start)

                                            # Fit on training data
                                            model.fit(x_train, y_train)

                                            utils.get_better_metrics(self.algo_mode, model, x_test, y_test, hyper_parameters, metrics)
                                            # Stores every run for hyper-parameters
                                            utils.classification_report_csv(self.algo_mode, data_type, technique, metrics)

                # Stores the best after tunning hyper-parameters    
                # utils.classification_report_csv(self.algo_mode, data_type, technique, metrics)

                print("computation for", technique , "is done")