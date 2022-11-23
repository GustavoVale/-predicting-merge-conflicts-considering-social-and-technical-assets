import os
import errno
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, cohen_kappa_score, \
    confusion_matrix, classification_report, recall_score, roc_auc_score
from datetime import datetime

column_names = ["Index", "Data_Type", "Model", "Sampling_Method", "Accuracy", "Precision", "Recall", "F1-Score", "AUC", "RECALL", "HYPER_PARAMETERS"]
csv_data = pd.DataFrame(columns=column_names)
report_data = []
pca_report_data = []

def create_directory(path):
    # create folder case it does not exist
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

def get_path(data_type):
    
    if data_type == 'both':
        return '../output/both_tech_and_social_data/'
    elif data_type == 'social':
        return '../output/social_data/'
    elif data_type == 'tech':
        return '../output/tech_data/'

    return ''

def get_data_train(balancing_technique, path):

    if balancing_technique == 'Under':
        return pd.read_csv(path + 'RandomUnderSampling_datatrain.csv')
    elif balancing_technique == 'Over':
        return pd.read_csv(path + 'RandomOverSampling_datatrain.csv')
    elif balancing_technique == 'Both':
        return pd.read_csv(path + 'RandomOver&UnderSampling_datatrain.csv')
    elif balancing_technique == 'Smote':
        return pd.read_csv(path + 'SMOTE_datatrain.csv')
    elif balancing_technique == 'BorderlineSmote':
        return pd.read_csv(path + 'BorderlineSMOTE_datatrain.csv')
    elif balancing_technique == 'SVMSmote':
        return pd.read_csv(path + 'SVMSMOTE_datatrain.csv')
    elif balancing_technique == 'Adasyn':
        return pd.read_csv(path + 'ADASYN_datatrain.csv')

    return ''

def get_x_y_train_and_test_data(data_train, path, lstm_or_gru = False, data_index = 0):
    
    # Shuffle the data
    data_train = data_train.sample(frac=1)
    
    data_test = pd.read_csv( path + 'data_test.csv')

    train = data_train.loc[:, ~data_train.columns.str.contains('^Unnamed')]
    test = data_test.loc[:, ~data_test.columns.str.contains('^Unnamed')]

    if lstm_or_gru:
        ttrain = train.values
        ttest = test.values

        y_train = ttrain[:, data_index]
        x_train = ttrain[:, 0:data_index]

        y_test = ttest[:, data_index]
        x_test = ttest[:, 0:data_index]

        x_train = np.reshape(x_train, (x_train.shape[0], 1, x_train.shape[1]))
        x_test = np.reshape(x_test, (x_test.shape[0], 1, x_test.shape[1]))
    
    else:

        y_train = train.has_conflict.copy()
        x_train = train.drop(['has_conflict'], axis=1)

        y_test = test.has_conflict.copy()
        x_test = test.drop(['has_conflict'], axis=1)

    return y_train, x_train, y_test, x_test

def get_num_cols(data_type):
    if data_type == 'both':
        return 29 
    elif data_type == 'social':
        return 16 

    return 13

def get_better_metrics(classifier, model, x_test, y_test, hyper_parameters, metrics):
    y_test_pred = model.predict(x_test)
    y_test_pred = y_test_pred.reshape(y_test_pred.shape[0], )

    if classifier == 'Decision_tree' or classifier == 'Random_forest' or classifier == 'SVM' or classifier == 'KNN':
        yhat_probs = model.predict(x_test)
    else:
        yhat_probs = model.predict(x_test, verbose=0)
        yhat_probs = yhat_probs[:, 0]

    recall = round(recall_score(y_test, y_test_pred.round(), average="micro"), 2)
    accuracy = round(accuracy_score(y_test, y_test_pred.round()), 2)
    auc = round(roc_auc_score(y_test, yhat_probs), 2)
    report = classification_report(y_test, y_test_pred.round())

    # Keeps commented to store the current result
    #if recall > metrics.recall:
    #    metrics.update_values(recall, accuracy, model, hyper_parameters, auc, report)
    #if recall == metrics.recall and accuracy > metrics.accuracy:
    #    metrics.update_values(recall, accuracy, model, hyper_parameters, auc, report)

    metrics.update_values(recall, accuracy, model, hyper_parameters, auc, report)

def classification_report_csv(classifier, model, sampling_method, metrics):
    lines = metrics.report.split('\n')
    #print(type(lines))
    row_count = 0
    for line in lines[2:-3]:
        #print(row_count)
        if row_count < 2:
            row = []
            row = line.split(' ')
            row = list(filter(None, row))
            if len(row) != 0:
                #print(classifier, model, sampling_method, row[0], accuracy, row[1], row[2], row[3], auc)
                values = [classifier, model, sampling_method, row[0], metrics.accuracy, row[1], row[2], row[3], metrics.auc, metrics.recall, metrics.hyper_parameters]
                report_data.append(values)
                row_count = row_count + 1


def classification_report_csv_df():
    dataframe = pd.DataFrame(data=report_data, columns=column_names)
    # print(dataframe)

    # datetime object containing current date and time
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")
    file_name = '../output/utils/classification_report-' + dt_string + '.csv'

    create_directory("../output/utils/")
    dataframe.to_csv(file_name, index=False)
