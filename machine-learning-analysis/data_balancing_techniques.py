import utils
import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import SMOTE, ADASYN, BorderlineSMOTE, SVMSMOTE, RandomOverSampler


def run(data_to_run, balancing_techniques):

    main_data = pd.read_csv('../data/ms-data.csv', index_col=0)

    # Getting columns
    social_columns = ['top_proj', 'top_proj_target', 'top_proj_source', 'occ_proj', 'occ_proj_target', 'occ_proj_source',
            'top_ms', 'top_ms_target', 'top_ms_source', 'occ_ms', 'occ_ms_target', 'occ_ms_source', 
            'devs', 'devs_target', 'devs_source', 'devs_both']

    tech_columns = ['files', 'files_target', 'files_source', 'files_both', 'chunks', 'chunks_target', 'chunks_source',
            'loc', 'loc_target', 'loc_source', 'commits', 'commits_target', 'commits_source']

    dependent_var_col = ['has_conflict']

    if 'both' in data_to_run:
        # Keeping only relevant data
        both_tech_and_social_data = main_data[
            dependent_var_col + social_columns + tech_columns
        ]
        balancing_data(both_tech_and_social_data, '../output/both_tech_and_social_data/', social_columns + tech_columns, balancing_techniques)

        print('\nboth_tech_and_social_data balanced\n')
    
    if 'social' in data_to_run:
        # Keeping only relevant data
        social_data = main_data[
            dependent_var_col + social_columns
        ]
        balancing_data(social_data, '../output/social_data/', social_columns, balancing_techniques)

        print('\nsocial_data balanced\n')
    
    if 'tech' in data_to_run:
        # Keeping only relevant data
        tech_data = main_data[
            dependent_var_col + tech_columns
        ]
        balancing_data(tech_data, '../output/tech_data/', tech_columns, balancing_techniques)

        print('\ntech_data balanced\n')


def balancing_data(data, path, columns, balancing_techniques):

    utils.create_directory(path)

    # Shuffle Data
    data = data.sample(frac=1)

    y = data.has_conflict.copy()
    x = data.drop(['has_conflict'], axis=1)

    # Splitting dataset into train and test
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=123)
    x_train.shape, x_test.shape
    
    # Combining Test data
    data_test = x_test
    data_test['has_conflict'] = y_test

    # Balancing the data using the balancing_techniques
    if 'Under' in balancing_techniques:
        under_sampling(x_train, y_train, path, columns)
    if 'Over' in balancing_techniques:
        over_sampling(x_train, y_train, path, columns)
    if 'Both' in balancing_techniques:
        over_under_sampling(x_train, y_train, path, columns)
    if 'Smote' in balancing_techniques:
        smote(x_train, y_train, path, columns)
    if 'BorderlineSmote' in balancing_techniques:
        borderline_smote(x_train, y_train, path, columns)
    if 'SVMSmote' in balancing_techniques:
        svm_smote(x_train, y_train, path, columns)
    if 'Adasyn' in balancing_techniques:
        adasyn(x_train, y_train, path, columns)

    # Write CSV for the test data
    data_test.to_csv( path + 'data_test.csv')


def numpy_to_df(x, y, columns):
    y_df = pd.DataFrame(y, columns=['has_conflict'])
    main_df = pd.DataFrame(x, columns=columns)
    main_df['has_conflict'] = y_df

    return main_df


def under_sampling(x, y, path, columns):
    undersample = RandomUnderSampler(sampling_strategy='majority')
    x_under, y_under = undersample.fit_resample(x, y)
    
    # Write CSV
    main_df = numpy_to_df(x_under, y_under, columns)
    main_df.to_csv(path + 'RandomUnderSampling_datatrain.csv')


def over_sampling(x, y, path, columns):
    oversample = RandomOverSampler(sampling_strategy='minority')
    x_over, y_over = oversample.fit_resample(x, y)
    
    # Write CSV
    main_df = numpy_to_df(x_over, y_over, columns)
    main_df.to_csv(path + 'RandomOverSampling_datatrain.csv')


def over_under_sampling(x, y, path, columns):
    over = RandomOverSampler(sampling_strategy=0.1)
    x, y = over.fit_resample(x, y)

    under = RandomUnderSampler(sampling_strategy=0.5)
    x, y = under.fit_resample(x, y)
    
    # Write CSV
    main_df = numpy_to_df(x, y, columns)
    main_df.to_csv(path + 'RandomOver&UnderSampling_datatrain.csv')


def smote(x, y, path, columns):
    oversample = SMOTE()
    x, y = oversample.fit_resample(x, y)
    
    # Write CSV
    main_df = numpy_to_df(x, y, columns)
    main_df.to_csv(path + 'SMOTE_datatrain.csv')


def borderline_smote(x, y, path, columns):
    oversample = BorderlineSMOTE()
    x, y = oversample.fit_resample(x, y)
    
    # Write CSV
    main_df = numpy_to_df(x, y, columns)
    main_df.to_csv(path + 'BorderlineSMOTE_datatrain.csv')


def svm_smote(x, y, path, columns):
    oversample = SVMSMOTE()
    x, y = oversample.fit_resample(x, y)
    
    # Write CSV
    main_df = numpy_to_df(x, y, columns)
    main_df.to_csv(path + 'SVMSMOTE_datatrain.csv')


def adasyn(x, y, path, columns):
    oversample = ADASYN()
    x, y = oversample.fit_resample(x, y)
    
    # Write CSV
    main_df = numpy_to_df(x, y, columns)
    main_df.to_csv(path + 'ADASYN_datatrain.csv')
