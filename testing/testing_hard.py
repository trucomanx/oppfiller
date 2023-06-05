#!/usr/bin/python

import os
import sys
sys.path.append('../src');

import OppFiller.Filler as oppmg
import OppFiller.Functions as oppf
import pandas as pd
import numpy as np
import csv


dataset_path='../dataset/1-raw/full_body.csv';
nholes=10;



df=pd.read_csv(dataset_path);

print('df.shape',df.shape);

obj=oppmg.Filler(model_type='sequence1');

for nth_row in range(3):
    row = df.iloc[nth_row]
    np_row=row.to_numpy();
    
    print(np_row)
    
    row_x=oppf.drop_n_elements_randomly_in_row_data(np_row,nholes);
    
    new_row=obj.FillRowData(row_x);
    
    out=np_row.reshape((34,1));
    out=np.append(out,  row_x.reshape((34,1)), axis=1);
    out=np.append(out,new_row.reshape((34,1)), axis=1);

    print(out)

