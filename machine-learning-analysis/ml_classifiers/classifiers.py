import utils


class Classifiers:
    """ 
    Executes the machine learning classifiers
    ...
    Attributes
    ----------
    data_types : list(str)
        type of data to perform analysis. Valid options: both, social, tech
    balancing_techniques : list(str)
        methods for data balancing you want to run the app. Valid options: Under, Over, Both, Smote, BorderlineSmote, SVMSmote, Adasyn
    classifiers : list(str)
        machine learning classifiers. Valid options: Decision_tree, Random_forest, KNN, SVM, DNN_MLP, DNN_SEQ, LSTM_MLP, LSTM_SEQ, GRU_MLP, GRU_SEQ

    Methods
    -------
    __run():
        Run the machine learning classifiers depending on the input attributes
    
    """
    
    def __init__(self, classifiers) -> None:
        self.classifiers = classifiers
        self.__run()

    def __run(self):
        for key in self.classifiers:
            value = self.classifiers[key]
            value.run()

        # Stores data in csv
        utils.classification_report_csv_df()
