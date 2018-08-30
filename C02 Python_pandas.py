'''
read the data without open() and close()
'''
import numpy as np
import pandas as pd

#load csv 
data_csv = pd.read_csv('iris.csv') 

#all data in the csv
print(data_csv)

#the error_all_test_data value in the csv
print(data_csv['all_test_data_acc'])

#delete the data when error_all_test_data != 1 
outfile = data_csv[data_csv['all_test_data_acc']!=1]

print(outfile)

#save a new csv
outfile.to_csv('iris_new1.csv', index=False)
