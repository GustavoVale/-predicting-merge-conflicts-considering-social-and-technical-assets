from operator import mod
from sklearn.metrics import auc

class Metrics:
    def __init__(self):
                self.recall = -0.99
                self.accuracy = -0.99
                self.model = None
                self.hyper_parameters = None
                self.auc = 0
                self.report = None

    def update_values(self, recall, accuracy, model, hyper_parameters, auc, report):
        self.recall = recall
        self.accuracy = accuracy
        self.model = model
        self.hyper_parameters = hyper_parameters
        self.auc = auc
        self.report = report