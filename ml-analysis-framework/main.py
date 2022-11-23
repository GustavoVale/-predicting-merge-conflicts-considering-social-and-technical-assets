#!/usr/bin/python
 
from ml_classifiers.classifiers import Classifiers
from handling_user_input import Handling_user_input

import argparse
#import data_modelling
#import chi_square_test
import data_balancing_techniques

# Creates a parser
parser = argparse.ArgumentParser(
    description = 'Console program to prepare data and run machine learning classifiers. See details in README.md', 
    prog='machine_learning', 
    usage='%(prog)s <running_mode> <json file with configuration to run>'
)

# Adds the four possible arguments
parser.add_argument('--research_questions', '-rqs', action='store_true', help='run research question analysis mode.')
parser.add_argument('--chi_square_test', '-chi', action='store_true', help='run chi square tests mode.')
parser.add_argument('--data_balancing', '-bal', action='store', help='run data balancing mode.')
parser.add_argument('--classifiers', '-class', action='store', help='start the app in classifying mode.')

args = vars(parser.parse_args())
got_run_mode = False

# if valid argument process
if args["research_questions"]:
    got_run_mode = True
    print("\n Running research_questions mode.\n")
    print("Sorry this option is not working properly!")
    # The input data changed. Hence, the data columns need to be updated.
    # data_modelling.research_question()

if args['chi_square_test']:
    got_run_mode = True
    print("\n Running chi_square_test mode.\n")
    print("Sorry this option is not working properly!")
    # The input data changed. Hence, the data columns need to be updated.
    # chi_square_test.run()

if args['data_balancing'] or args['classifiers']:
    hui = Handling_user_input()
    
    got_run_mode = True
    
    if args['data_balancing']:
        print("\n Running data_balancing mode.\n")
        hui.handling_user_input(args, 'data_balancing')
        data_balancing_techniques.run(hui.data_types, hui.balancing_techniques) 

    if args['classifiers']:
        print("\n Running classifiers mode.\n")
        hui.handling_user_input(args, 'classifiers')
        Classifiers(hui.classifiers)

if got_run_mode:
    print("\n\nCode executed successfully!!!\n\n")
else:
    print("\n\nPlease, choose a valid option!\n\n")

