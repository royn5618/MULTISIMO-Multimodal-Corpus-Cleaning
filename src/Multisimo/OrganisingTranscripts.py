'''
Created on 15 Mar 2018

@author: Owner
'''
import numpy as np
import pandas as pd
import os
from pandas import ExcelWriter
from pandas import DataFrame

root_path = "$/Multisimo/Multisimo_Data/transcripts_text"
raw_excel = pd.read_excel('$/Multisimo/Multisimo_Data/basic_format.xlsx')
list_IDs = raw_excel['ID'].tolist()
list_IDs_copy = raw_excel['ID'].tolist()
files = os.listdir(root_path)
for file in files:
    file = open(root_path + "/" + file , "r")
    raw_transcripts = file.readlines()
    for item in raw_transcripts:
        for each_id in list_IDs:
            if each_id in item:
                index = list_IDs.index(each_id)
                value = list_IDs_copy[index]
                list_IDs_copy[index] = value + item

df_transcripts = DataFrame({'test_set': list_IDs_copy})

writer = ExcelWriter('PythonExport.xlsx')
df_transcripts.to_excel(writer)
writer.save()
print('done')
