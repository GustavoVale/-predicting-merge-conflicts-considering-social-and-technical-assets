from sklearn.tree import DecisionTreeClassifier
import utils
from ml_classifiers.metrics_entity import Metrics

class Decision_tree:

    def __init__(self, dictionary, data_types, balancing_techniques, algo_mode) -> None:
            self.data_types = data_types
            self.balancing_techniques = balancing_techniques
            self.algo_mode = algo_mode

            self.max_depths = dictionary.get("max_depths", None)
            self.max_features = dictionary.get("max_features", None)
            self.min_samples_leaves = dictionary.get("min_samples_leaves", None)
            self.min_samples_splits = dictionary.get("min_samples_splits", None)
            self.criteria = dictionary.get("criteria", None)
            self.splitters = dictionary.get("splitters", None)
            
            self.is_valid_object = self.__is_valid_object()

    def __is_valid_object(self):
        return None not in [self.max_depths, self.max_features, self.min_samples_leaves, self.min_samples_splits, self.criteria, self.splitters]

    def run(self):
        print('\n DECISION TREE is running\n')
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
                                for criterion in self.criteria:
                                    for splitter in self.splitters:

                                        hyper_parameters = "max_depth:", max_depth, " max_feature:", max_feature, " min_samples_leaf:", min_samples_leaf, \
                                            " min_samples_split:", min_samples_split, " criterion:", criterion, " splitter:", splitter

                                        model = DecisionTreeClassifier(criterion=criterion, max_depth=max_depth,
                                        min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf, splitter=splitter)

                                        # Fit on training data
                                        model.fit(x_train, y_train)

                                        utils.get_better_metrics(self.algo_mode, model, x_test, y_test, hyper_parameters, metrics)
                                        # Stores every run for hyper-parameters
                                        utils.classification_report_csv(self.algo_mode, data_type, technique, metrics)

                # Stores the best after tunning hyper-parameters    
                # utils.classification_report_csv(self.algo_mode, data_type, technique, metrics)

                print("computation for", technique , "is done")
