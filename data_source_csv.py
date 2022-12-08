import pandas as pd
import os

# Making a list of all sales data's file name
file_names = [file for file in  os.listdir('data_source')]

# Make directory to save files
cmd = 'mkdir data_source_csv'
os.system(cmd)

# Read and Convert data into csv
for file_name in file_names:
    data = pd.read_excel('data_source/'+file_name)
    data.to_csv('data_source_csv/'+file_name+'.csv', index=False)
    print('Finish Converting '+file_name)