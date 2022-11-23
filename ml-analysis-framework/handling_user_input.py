import json
from processing_files import get_file_content
from ml_classifiers.decision_tree import Decision_tree
from ml_classifiers.DNN import DNN
from ml_classifiers.random_forest import Random_forest
from ml_classifiers.KNN import KNN
from ml_classifiers.SVM import SVM
from ml_classifiers.GRU import GRU
from ml_classifiers.LSTM import LSTM

class Handling_user_input:
    """ 
    Handles the json file provided by the user
    ...
    Attributes
    ----------
    running_mode : str
        mode application is running
    data_types : list(str)
        type of data to perform analysis. Valid options: both, social, tech
    balancing_techniques : list(str)
        methods for data balancing you want to run the app. Valid options: Under, Over, Both, Smote, BorderlineSmote, SVMSmote, Adasyn
    classifiers : dictionary(machine_learning_classifiers)
        machine learning classifiers. Valid options: Random_forest, KNN, SVM, DNN_MLP, DNN_SEQ, LSTM_MLP, LSTM_SEQ, GRU_MLP, GRU_SEQ

    Methods
    -------
    handling_user_input(input_args, running_mode):
        Handles the dictionary of input arguments for a running mode, mapping it to the class attributes when existing
    
    """
    
    def __init__(self) -> None:
        self.running_mode = None
        self.data_types = []
        self.balancing_techniques = []
        self.classifiers = {}

    def __extract_objects_from_json(self, file_name):
        """ 
        Returns objects from a json file taking the file name
        """
        try:
            return json.loads(get_file_content(file_name))
        except:
            print('Failing parsing json file')
            raise 
    
    def __filtering_data_types(self, data_types):
        """ 
        Filters data types based on valid options
        """
        valid_options = ['both', 'social', 'tech']
        return list(set(valid_options).intersection(data_types))

    def __filtering_balancing_techniques(self, balancing_techniques):
        """ 
        Filters balancing techniques based on valid options
        """
        valid_options = ['Under', 'Over', 'Both', 'Smote', 'BorderlineSmote', 'SVMSmote', 'Adasyn']
        return list(set(valid_options).intersection(balancing_techniques))

    def __filtering_classifiers(self, classifiers):
        """ 
        Filters classifiers based on valid options
        """
        valid_options = ['Decision_tree', 'Random_forest', 'KNN', 'SVM', 'DNN_MLP', 'DNN_SEQ', 'LSTM_MLP', 'LSTM_SEQ', 'GRU_MLP', 'GRU_SEQ']
        return list(set(valid_options).intersection(classifiers))

    def __raise_error(self):
        """
        Raises error
        """
        print("\nThe input file does not have all required fields\n")
        raise

    def __mapping_configurations(self, dictionary):
        """ 
        Maps dictionary keys if existing to class attributes
        """
        
        if "data_types" in dictionary:
            self.data_types = self.__filtering_data_types(dictionary["data_types"])
        
        if "balancing_techniques" in dictionary:
            self.balancing_techniques = self.__filtering_balancing_techniques(dictionary["balancing_techniques"])
        
        if "classifiers" in dictionary:
            choosen_classifiers = self.__filtering_classifiers(dictionary["classifiers"])

        for classifier in choosen_classifiers:
            curr_val = dictionary[classifier]
            if curr_val:
                if classifier == "Decision_tree":
                    dt = Decision_tree(curr_val, self.data_types, self.balancing_techniques, classifier)
                    if not dt.is_valid_object:
                        self.__raise_error()
                    self.classifiers[classifier] = dt

                if classifier == "Random_forest":
                    rf = Random_forest(curr_val, self.data_types, self.balancing_techniques, classifier)
                    if not rf.is_valid_object:
                        self.__raise_error()
                    self.classifiers[classifier] = rf

                if classifier == "KNN":
                    knn = KNN(curr_val, self.data_types, self.balancing_techniques, classifier)
                    if not knn.is_valid_object:
                        self.__raise_error()
                    self.classifiers[classifier] = knn

                if classifier == "SVM":
                    svm = SVM(curr_val, self.data_types, self.balancing_techniques, classifier)
                    if not svm.is_valid_object:
                        self.__raise_error()
                    self.classifiers[classifier] = svm
                    
                if classifier == "DNN_MLP" or classifier == "DNN_SEQ":
                    dnn = DNN(curr_val, self.data_types, self.balancing_techniques, classifier)
                    if not dnn.is_valid_object:
                        self.__raise_error()
                    self.classifiers[classifier] = dnn

                if classifier == "LSTM_MLP" or classifier == "LSTM_SEQ":
                    lstm = LSTM(curr_val, self.data_types, self.balancing_techniques, classifier)
                    if not lstm.is_valid_object:
                        self.__raise_error()
                    self.classifiers[classifier] = lstm

                if classifier == "GRU_MLP" or classifier == "GRU_SEQ":
                    gru = GRU(curr_val, self.data_types, self.balancing_techniques, classifier)
                    if not gru.is_valid_object:
                        self.__raise_error()
                    self.classifiers[classifier] = gru

    def __report_if_input_is_invalid(self):
        """ 
        Reports a valid input or raise error
        """
        if self.running_mode == "data_balancing" and self.data_types and self.balancing_techniques:
            print("\nValid input\n")
        elif self.running_mode == "classifiers" and self.data_types and self.balancing_techniques and self.classifiers:
            print("\nValid input\n")
        else:
            self.__raise_error()

    def handling_user_input(self, input_args, running_mode):
        """ 
        Handles the dictionary of input arguments for a running mode, mapping it to the class attributes when existing
        """

        self.running_mode = running_mode
        
        dictionary = self.__extract_objects_from_json(input_args[self.running_mode])
        
        self.__mapping_configurations(dictionary)
        
        self.__report_if_input_is_invalid()
  