#!/bin/bash
# Purpose: A simple shell script to install required libraries to run the application
# Usage: ./install_libraries.sh
# --
# Author: Gustavo Vale under GPL v2.x+
# Last updated: 28/Mar/2022
# --------------------------------------------------------------------------------

RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'

# To create and activate tensorflow environment:
echo "\n Creating tensorflow environment for Python 3.7\n"
conda create -n tensorflow python=3.7
echo "\n Acitivating tensorflow environment\n"
conda activate tensorflow

# To install numpy:
echo "\n ${CYAN}Installing numpy ${NC}\n"
pip install numpy

# To install pandas:
echo "\n ${CYAN}Installing pandas ${NC}\n"
pip install pandas

# To install matplotlib:
echo "\n ${CYAN}Installing matplotlib ${NC}\n"
pip install matplotlib

# To install seaborn:
echo "\n ${CYAN}Installing seaborn ${NC}\n"
pip install seaborn

# To install sklearn:
echo "\n ${CYAN}Installing sklearn ${NC}\n"
pip install sklearn

# To install imblearn:
echo "\n ${CYAN}Installing imblearn ${NC}\n"
pip install imblearn

# To install tensorflow:
echo "\n ${CYAN}Installing tensorflow ${NC}\n"
pip install tensorflow

# To install statsmodels:
echo "\n ${CYAN}Installing statsmodels ${NC}\n"
pip install statsmodels

# To install ax:
echo "\n ${CYAN}Installing ax ${NC}\n"
pip install ax

# To install ax-platform:
echo "\n ${CYAN}Installing ax-platform ${NC}\n"
pip install ax-platform

# To install IPython:
echo "\n ${CYAN}Installing IPython ${NC}\n"
pip install IPython

# To install keras-metrics:
echo "\n ${CYAN}Installing keras_metrics ${NC}\n"
pip install keras-metrics

echo "\n ${CYAN}Document got to the end.${NC}"
echo "\n ${RED}Please, check if everything was installed correctly. ${NC}\n"

