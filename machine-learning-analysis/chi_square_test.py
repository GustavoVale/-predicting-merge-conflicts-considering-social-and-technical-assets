import utils
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

def run():

    utils.create_directory("../output/chitest/")

    columnnames = ["Analysis", "Chi-squared", "dof", "P-value"]
    maindata = []

    # The values below were removed from the ../output/RQ1.1_Results.csv
    first_analysis = list(chi_square_test_two_variables(45297, 3290, 60609, 3409))
    first_values = ['First', first_analysis[0], first_analysis[1], first_analysis[2]]
    maindata.append(first_values)

    # The values below were removed from the ../output/RQ1.2_Results.csv
    second_analysis = list(chi_square_test_two_variables(78740, 3950, 30003, 2800))
    second_values = ['Second', second_analysis[0], second_analysis[1], second_analysis[2]]
    maindata.append(second_values)

    # The values below were removed from the ../output/RQ2.2_Results.csv
    third_analysis = list(chi_square_test_four_variables(40249, 2912, 15069, 1569, 52392, 2674, 26788, 2617))
    third_values = ['Third', third_analysis[0], third_analysis[1], third_analysis[2]]
    maindata.append(third_values)

    df = pd.DataFrame(maindata, columns=columnnames)
    df.to_csv('../output/chitest/ChiSquareTest.csv')


def chi_square_test_two_variables(ms1, cms1, ms2, cms2):
    data_array = np.array([[ms1, cms1], [ms2, cms2]])
    df = pd.DataFrame(data_array, columns=["No Conflicts", "Conflicts"])
    df.index = ["Top", "Occ"]
    value = calculation_chi_square(df)
    return value


def chi_square_test_four_variables(ms1, cms1, ms2, cms2, ms3, cms3, ms4, cms4):
    data_array = np.array([[ms1, cms1], [ms2, cms2], [ms3, cms3], [ms4, cms4]])
    df = pd.DataFrame(data_array, columns=["No Conflicts", "Conflicts"])
    df.index = ["Top", "TopOcc", "OccTop", "Occ"]
    value = calculation_chi_square(df)
    return value


def calculation_chi_square(df):
    statistics, p_value, dof, exp = chi2_contingency(df, correction=False)
    # print("Chi-squared: " + str(statistics))
    # print("Degree of Freedom: ", dof)
    # print("P-value: " + str(p_value))
    return statistics, dof, p_value
