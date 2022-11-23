# Social and Technical Analysis for Predicting Merge Conflicts - Machine Learning Analysis

Console app to prepare and analyse data for predicting merge conflicts.  
You can run it in four modes: **research_questions**, **chi_square_test**, **data_balancing**, and **classifiers**.

## Pre-requisites

Make sure that you have Python3 and pip3 installed. The following libraries are also required: *tensorflow*, *numpy*, *pandas*, *matplotlib*, *seaborn*,  *sklearn*, *imblearn*, *statsmodels*, *ax*, *ax-platform*,  and *IPython*.

If you do not have all of them installed, we created a shell script that installs them for you. Just run:
```
sh install_libraries.sh
```

## How to run?

 For  **research_questions** and **chi_square_test** modes, just run the main.py file passing the argument of the mode. For instance, to run the research_questions mode, run:

```
python3 main.py -rqs
```
For **data_balancing** and **classifiers** modes, two arguments are required as described below.

1. Running mode: *bal* or *data_balancing* for the **data_balancing mode** and *class* or *classifiers* for the **classifiers mode**.
2. Configuration file: pass the path of the configuration file. 

For instance, running from the current directory is expected something like:
```
python3 main.py -class sample_simple_options.json
``` 

## What should the configuration file look like? 

As seen in the example, it is expected a json file.
For the monitoring mode, something like:
```
{
	"data_types": ["social"],
	"balancing_techniques": ["Under"],
	"classifiers": ["Decision_tree", "Random_forest", "KNN", "SVM", "DNN_MLP", "DNN_SEQ", "LSTM_MLP", "LSTM_SEQ", "GRU_MLP", "GRU_SEQ"]
}
```
**Obs**: `data_types` and `balancing_techniques` are mandatory for both modes and `classifiers` is mandatory to the classifiers mode. 

## What all of these parameters represent? 

Alphabetically sorted: 
-  **data_types** - type of data to perform analysis. Three valid options: both, social, tech.
-  **balancing_techniques**  - methods for data balancing you want to run the app. Seven valid options: Under, Over, Both, Smote, BorderlineSmote, SVMSmote, Adasyn.
-  **classifiers** - machine learning classifiers. Ten valid options: Decision_tree, Random_forest, KNN, SVM, DNN_MLP, DNN_SEQ, LSTM_MLP, LSTM_SEQ, GRU_MLP, GRU_SEQ. 

**Obs:** Note that for the deep learning methods (DNN, LSTM, and GRU), it runs with multilayer perceptron (MLP) and sequential (SEQ).

## Files Description

In the machine-learning-analysis directory, you will find:
- `miscellaneous`  folder - contains files from previous versions of the application that belong to the main functionality, but might be useful. 
- `ml_classifiers` folder - contains all files necessary to run the classifiers.  It includes the six classifiers (DNN.py, GRU.py, KNN.py, LSTM.py, random_forest.py, SVM.py) and helper files, such as classifiers.py and keras_helper.py. The former calls the classifiers when present in the input file and the last is called by the DNN, LSTM, and GRU classifiers. 
- `.gitignore` file  - with file paths to ignore (e.g., the generated log files).
- `chi_square_test.py` file - runs the chi square test to the data since it is usually unpaired and variables are categorical.
- `data_balancing_techniques.py` file - provides techniques for data balancing such as *Random sampling* (over, under and combine over_under sampling) and *synthetic sampling* (SMOTE, Borderline SMOTE, ADASYN, and SVM-SMOTE).
- `data_modelling.py` file - processes the input data to answer the first two research questions.
- `handling_user_input.py` file - handles the json file provided by the user.
- `install_libraries.sh` file - shell script to support required libraries installation. 
- `main.py` file - the executable file to run the application.
- `processing_files.py` file - deals with reading and writing files.
- `README.md` file - this file.
- `sample_full_options.json` file - sample file to support the user a quick starter with all possible configurations.
- `sample_simple_options.json` file - sample file to support the user a quick starter with a simplified number of configurations.
- `utils.py` file - contains useful functions to support classifiers and other features avoiding duplication of code. 

**Obs:** Right now the application expects a **ms-data.csv** file with 30 metrics. Look at the file. Each column represents a metric. It is located in the upper folder inside data folder.

## Improvements/ TODOS
There are some points of improvement for the application
1. Update the `data_modelling.py` file to make the **research_questions** mode work properly.
2. Update the `chi_square_test.py` file to make the **chi_square_test** mode work properly.
3. Make the application flexible enough to run with different input files. 
