import pygame as pg
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pandas
import csv
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
#from Build_Graph.py import *
from Excel_Read import *
from Transform_to_Latex import *
from Gysto import *



print('what will we build?')
print('graphics = a, tables = b, (histograms = c)')
desired = input()

if desired == 'a':
    execute_Excel_Read()
elif desired == 'b':  
    read_csv(file_name)
    make_latex_table_with_borders(data)
    make_latex_table_without_borders(data)
    make_latex_table_with_separator_between_columns(data)
    
    print('Введите фиксированную длину столбца')
    len_array = [int(input()) for _ in range(3)]

    make_latex_table_with_length_columns(data, len_array)
    
elif desired == 'c':
   
    print('Введите n_bins')
    n_bins = int(input())
    Gysto(n_bins)
    
