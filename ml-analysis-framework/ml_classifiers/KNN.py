from sklearn.neighbors import KNeighborsClassifier
import utils
from ml_classifiers.metrics_entity import Metrics

class KNN:

    def __init__(self, dictionary, data_types, balancing_techniques, algo_mode) -> None:
            self.data_types = data_types
            self.balancing_techniques = balancing_techniques
            self.algo_mode = algo_mode
            
            self.n_neighbors = dictionary.get("n_neighbors", None)
            self.weights = dictionary.get("weights", None)
            self.metrics = dictionary.get("metrics", None)
            self.algorithms = dictionary.get("algorithms", None)
            
            self.is_valid_object = self.__is_valid_object()


    def __is_valid_object(self):
        return None not in [self.n_neighbors, self.weights, self.metrics, self.algorithms]

    def run(self):
        print('\nK Neighbors is running \n')
        
        for data_type in self.data_types:

            path = utils.get_path(data_type)

            for technique in self.balancing_techniques:
                data_train = utils.get_data_train(technique, path)

                y_train, x_train, y_test, x_test = utils.get_x_y_train_and_test_data(data_train, path)

                metrics = Metrics()
        
                # Hyper-parameters
                for n_neighbor in self.n_neighbors:
                    for weight in self.weights:
                        for measure in self.metrics:
                            for algorithm in self.algorithms:

                                hyper_parameters = "n_neighbors:", n_neighbor, " weights:", weight, " metrics:", measure, " algorithm", algorithm
                    
                                # Create the knn model
                                model = KNeighborsClassifier(n_neighbors=n_neighbor, weights=weight, metric=measure, algorithm=algorithm)

                                # Fit on training data
                                model.fit(x_train, y_train)

                                utils.get_better_metrics(self.algo_mode, model, x_test, y_test, hyper_parameters, metrics)

                                # Stores every run for hyper-parameters
                                utils.classification_report_csv(self.algo_mode, data_type, technique, metrics)

                # Stores the best after tunning hyper-parameters    
                # utils.classification_report_csv(self.algo_mode, data_type, technique, metrics)

                print("\ncomputation for", technique , "is done\n")
                