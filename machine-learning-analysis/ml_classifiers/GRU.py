import utils
import ml_classifiers.keras_helper as keras_helper
from ml_classifiers.metrics_entity import Metrics

class GRU:

    def __init__(self, dictionary, data_types, balancing_techniques, algo_mode) -> None:
            self.data_types = data_types
            self.balancing_techniques = balancing_techniques
            self.algo_mode = algo_mode
            
            self.learning_rates = dictionary.get("learning_rates", None)
            self.dropout_rates = dictionary.get("dropout_rates", None)
            self.units = dictionary.get("units", None)
            self.neurons_denses = dictionary.get("neurons_denses", None)
            self.hidden_layers = dictionary.get("hidden_layers", None)
            self.epochs = dictionary.get("epochs", None)
            self.batch_sizes = dictionary.get("batch_sizes", None)
            self.activations = dictionary.get("activations", None)
            
            self.is_valid_object = self.__is_valid_object()


    def __is_valid_object(self):
        return None not in [self.learning_rates, self.dropout_rates, self.units, self.neurons_denses, self.hidden_layers, 
        self.epochs, self.batch_sizes, self.activations]


    def run(self):

        algorithm, mode = self.algo_mode.split("_")
        
        print('\n' + self.algo_mode + ' is running\n')

        for data_type in self.data_types:

            path = utils.get_path(data_type)

            for technique in self.balancing_techniques:
                data_train = utils.get_data_train(technique, path)

                data_index = utils.get_num_cols(data_type)

                y_train, x_train, y_test, x_test = utils.get_x_y_train_and_test_data(data_train, path, True, data_index)

                metrics = Metrics()

                # Hyper-parameters
                for learning_rate in self.learning_rates:
                    for dropout_rate in self.dropout_rates:
                        for unit in self.units:
                            for neurons_dense in self.neurons_denses:
                                for hidden_layers in self.hidden_layers:
                                    for epochs in self.epochs:
                                        for batch_size in self.batch_sizes:
                                            for activation in self.activations:

                                                print(technique, learning_rate, dropout_rate, unit, neurons_dense, hidden_layers, epochs, batch_size,
                                                    activation)
                                                hyper_parameters = "learning_rate:", learning_rate, " dropout_rate:", dropout_rate, " unit:", unit, \
                                                    "neurons_dense:", neurons_dense, " hidden_layers:", hidden_layers, " epochs:", epochs, \
                                                    " batch_size:", batch_size, " activation:", activation
                                                
                                                datamodel = keras_helper.keras_model(algorithm, mode, learning_rate, dropout_rate, unit, neurons_dense, hidden_layers,
                                                                                epochs, batch_size, activation, x_train, y_train, data_index)


                                                utils.get_better_metrics(self.algo_mode, datamodel, x_test, y_test, hyper_parameters, metrics)
                                                
                                                # Stores every run for hyper-parameters
                                                utils.classification_report_csv(self.algo_mode, data_type, technique, metrics)

                # Stores the best after tunning hyper-parameters    
                # utils.classification_report_csv(self.algo_mode, data_type, technique, metrics)

                print("\ncomputation for", technique , "is done\n")

