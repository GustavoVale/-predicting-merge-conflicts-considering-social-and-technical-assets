from imblearn.over_sampling import ADASYN, SMOTE
import pandas as pd
from sklearn.preprocessing import StandardScaler
import itertools
import statsmodels.api as sm
from numpy import mean, var
import scipy.stats as stats
from math import sqrt
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import precision_recall_curve, auc, roc_curve, roc_auc_score

# TODO: NOT USED SO FAR
def standardized_data(X, y):
    sc = StandardScaler()
    X = sc.fit_transform(X)
    y = sc.transform(y)

    return X, y

# TODO: NOT USED SO FAR
def dataVisualization(_dataframe, _feature):
    print(_dataframe[_feature].value_counts())

    if (_feature == 'Experience'):
        sns.barplot(x="Experience", y="conflt", data=_dataframe)

        Beginnercnflt = _dataframe["conflt"][_dataframe["Experience"] == 'Beginner'].value_counts(normalize=True)[
                            1] * 100
        intermediatecnflt = \
            _dataframe["conflt"][_dataframe["Experience"] == 'Intermediate'].value_counts(normalize=True)[1] * 100
        advancecnflt = _dataframe["conflt"][_dataframe["Experience"] == 'Advanced'].value_counts(normalize=True)[
                           1] * 100

        print("Percentage of Beginner caused conflicts:", round(Beginnercnflt, 2))
        print("Percentage of Intermediate caused conflicts:", round(intermediatecnflt, 2))
        print("Percentage of Advanced caused conflicts:", round(advancecnflt, 2))
        plt.savefig('Experience.png')

        bgcnflt = (3573 / 9117) * 100
        intcnflt = (868 / 9117) * 100
        advcnflt = (4676 / 9117) * 100

        expcnflt = pd.DataFrame(
            {'Experience': ['Beginner', 'Advanced', 'Intermediate'], 'Conflict': [bgcnflt, advcnflt, intcnflt]})
        sns.barplot(x="Experience", y='Conflict', data=expcnflt)

        print("Beginner caused conflicts in total conflicts:", round(bgcnflt, 2), "%")
        print("Advanced caused conflicts in total conflicts:", round(advcnflt, 2), "%")
        print("Intermediate caused conflicts in total conflicts:", round(intcnflt, 2), "%")
        plt.savefig('Experience-Conflicts.png')

# TODO: NOT USED SO FAR
def setDataset(_dataframe, _target):
    dataframe = _dataframe
    X = None
    y = None

    if 'cont_id' in dataframe:
        dataframe = dataframe.drop(['cont_id'], axis=1)

    if _target == 'conflt':
        # print('conflt')
        dataframe = dataframe.drop(['ms_confl'], axis=1)
        y = dataframe.conflt.copy()
        X = dataframe.drop(['conflt'], axis=1)
    elif _target == 'ms_confl':
        # print('ms_confl')
        dataframe = dataframe.drop(['conflt'], axis=1)
        y = dataframe.ms_confl.copy()
        X = dataframe.drop(['ms_confl'], axis=1)
    return X, y

# TODO: NOT USED SO FAR
def smote(_X, _y):
    smt = SMOTE()
    X, y = smt.fit_sample(_X, _y)
    return X, y

# TODO: NOT USED SO FAR
def ad_smote(_X, _y):
    ada = ADASYN(random_state=130)
    X, y = ada.fit_sample(_X, _y)
    return X, y

# TODO: NOT USED SO FAR
# function to calculate Cohen's d for independent samples
def cohen_d(d1, d2):
    n1, n2 = len(d1), len(d2)
    s1, s2 = var(d1, ddof=1), var(d2, ddof=1)
    s = sqrt(((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2))
    u1, u2 = mean(d1), mean(d2)
    return (u1 - u2) / s

# TODO: NOT USED SO FAR
def logitSummary(_X, _y):
    logit_model = sm.Logit(_y, _X)
    result = logit_model.fit()
    print(result.summary())

# TODO: NOT USED SO FAR
def listwise_corr_pvalues(df, method):
    df = df.dropna(how='any')._get_numeric_data()
    dfcols = pd.DataFrame(columns=df.columns)
    pd.set_option('display.max_rows', None, 'display.max_columns', None)
    rvalues = dfcols.transpose().join(dfcols, how='outer')
    pvalues = dfcols.transpose().join(dfcols, how='outer')
    length = str(len(df))

    if method == None:
        test = stats.pearsonr
        test_name = "Pearson"
    elif method == "spearman":
        test = stats.spearmanr
        test_name = "Spearman Rank"
    elif method == "kendall":
        test = stats.kendalltau
        test_name = "Kendall's Tau-b"

    for r in df.columns:
        for c in df.columns:
            rvalues[r][c] = round(test(df[r], df[c])[0], 4)

    for r in df.columns:
        for c in df.columns:
            pvalues[r][c] = format(test(df[r], df[c])[1], '.4f')

    # print("Correlation test conducted using list-wise deletion",
    #       "\n",
    #       "Total observations used: ", length, "\n", "\n",
    #       f"{test_name} Correlation Values", "\n", rvalues, "\n",
    #       "Significant Levels", "\n", pvalues)

# TODO: NOT USED SO FAR
def pairwise_corr_pvalues(df, method=None):
    correlations = {}
    pvalues = {}
    length = {}
    columns = df.columns.tolist()

    if method == None:
        test = stats.pearsonr
        test_name = "Pearson"
    elif method == "spearman":
        test = stats.spearmanr
        test_name = "Spearman Rank"
    elif method == "kendall":
        test = stats.kendalltau
        test_name = "Kendall's Tau-b"

    for col1, col2 in itertools.combinations(columns, 2):
        sub = df[[col1, col2]].dropna(how="any")
        correlations[col1 + " " + "&" + " " + col2] = format(test(sub.loc[:, col1], sub.loc[:, col2])[0], '.4f')
        pvalues[col1 + " " + "&" + " " + col2] = format(test(sub.loc[:, col1], sub.loc[:, col2])[1], '.4f')
        length[col1 + " " + "&" + " " + col2] = len(df[[col1, col2]].dropna(how="any"))

    corrs = pd.DataFrame.from_dict(correlations, orient="index")
    corrs.columns = ["r value"]
    pvals = pd.DataFrame.from_dict(pvalues, orient="index")
    pvals.columns = ["p-value"]

    l = pd.DataFrame.from_dict(length, orient="index")
    l.columns = ["N"]

    results = corrs.join([pvals, l])
    # print(f"{test_name} correlation", "\n", results)


###### Code below was in the GRU.py and LSTM.py

def ROCCurve(x_test, y_test, model):  # works for sequential model
    # pred = model.predict_proba(x_test)
    pred = model.predict(x_test)
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    for i in range(2):
        fpr[i], tpr[i], _ = roc_curve(y_test, pred)
        roc_auc[i] = auc(fpr[i], tpr[i])

    print(roc_auc_score(y_test, pred))
    plt.figure()
    plt.plot(fpr[1], tpr[1])
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic')
    plt.show()


def PRCurve(x_test, y_test, model):  # works for sequential and LSTM
    yhat = model.predict(x_test)
    model_probs = yhat[:, 0]
    # calculate the precision-recall auc
    precision, recall, _ = precision_recall_curve(y_test, model_probs)
    auc_score = auc(recall, precision)
    print('Logistic PR AUC: %.3f' % auc_score)
    # plot precision-recall curves
    # plot model precision-recall curve
    precision, recall, _ = precision_recall_curve(y_test, model_probs)
    plt.plot(recall, precision, marker='.', label='Binary')
    # axis labels
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    # show the legend
    plt.legend()
    # show the plot
    plt.show()
