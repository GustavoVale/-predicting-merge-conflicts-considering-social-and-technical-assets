from sklearn import svm
import utils
from ml_classifiers.metrics_entity import Metrics

class SVM:

    def __init__(self, dictionary, data_types, balancing_techniques, algo_mode) -> None:
        print(dictionary)
        
        self.data_types = data_types
        self.balancing_techniques = balancing_techniques
        self.algo_mode = algo_mode

        self.cs = dictionary.get("cs", None)
        self.kernels = dictionary.get("kernels", None)
        self.gammas = dictionary.get("gammas", None)
        self.probabilities = dictionary.get("probabilities", None)
        self.decision_function_shapes = dictionary.get("decision_function_shapes", None)

        self.is_valid_object = self.__is_valid_object()

    def __is_valid_object(self):
        return None not in [self.cs, self.kernels, self.gammas, self.probabilities, self.decision_function_shapes]

    def run(self):
        print('\nSIMPLE VECTOR MACHINE is running \n')
        
        for data_type in self.data_types:

            path = utils.get_path(data_type)

            for technique in self.balancing_techniques:
                data_train = utils.get_data_train(technique, path)

                y_train, x_train, y_test, x_test = utils.get_x_y_train_and_test_data(data_train, path)

                metrics = Metrics()

                for c in self.cs:
                    for kernel in self.kernels:
                        for gamma in self.gammas:
                            for probability in self.probabilities:
                                for decision_function_shape in self.decision_function_shapes:

                                    hyper_parameters = "c:", c, " kernel:", kernel, " gamma:", gamma, " probability:", probability, " decision_function_shape:", decision_function_shape

                                    # Create the model with 100 trees
                                    svm_model = svm.SVC(C=c, kernel=kernel, gamma=gamma, probability=probability, decision_function_shape=decision_function_shape)

                                    # Fit on training data
                                    svm_model.fit(x_train, y_train)
                                    
                                    utils.get_better_metrics(self.algo_mode, svm_model, x_test, y_test, hyper_parameters, metrics)                               

                                    # Stores every run for hyper-parameters
                                    utils.classification_report_csv(self.algo_mode, data_type, technique, metrics)

                # Stores the best after tunning hyper-parameters    
                # utils.classification_report_csv(self.algo_mode, data_type, technique, metrics)

                print("\ncomputation for", technique , "is done\n")