#!/usr/bin/python

import sys
sys.path.append('../src');

import pandas as pd
import os
import csv
import random
from tqdm import tqdm 

import OppFiller.Functions as oppf

dataset_path='../dataset/1-raw/full_body.csv';
output_path='../dataset/2-data';
output_filename_x='data_normalized_x.csv';
output_filename_y='data_normalized_y.csv';
MAX_NHOLES=10;
ANGLE=25;


filepath_x = os.path.join(output_path,output_filename_x)
filepath_y = os.path.join(output_path,output_filename_y)


df = pd.read_csv(dataset_path);

filex=open(filepath_x, 'w', newline='\n')
filey=open(filepath_y, 'w', newline='\n')

writerx = csv.writer(filex)
writery = csv.writer(filey)

writerx.writerow(df.columns)
writery.writerow(df.columns)

L=df.shape[0];

for nth_row in tqdm(range(L)):
    row = df.iloc[nth_row];
    np_row = row.to_numpy();
    
    # data
    row_x  = np_row.copy();
    row_y  = np_row.copy();
    
    # normalization
    row_x_c,xc,yc,S = oppf.normalize_valid_row_data(row_x);
    row_y_c         = oppf.normalize_valid_row_data_with(row_y,xc,yc,S);
    
    # Writting
    writerx.writerow(row_x_c)
    writery.writerow(row_y_c)
    
    
    for nholes in range(1,1+MAX_NHOLES):
        # data augmentation
        ang=random.uniform(-ANGLE, ANGLE);
        row_x=oppf.centering_rotation_of_row_data(np_row,ang);
        row_y=row_x.copy();
        row_x=oppf.drop_n_elements_randomly_in_row_data(row_x,nholes);
        
        # normalization
        
        row_x_c,xc,yc,S = oppf.normalize_valid_row_data(row_x);
        row_y_c         = oppf.normalize_valid_row_data_with(row_y,xc,yc,S);
        
        # writing
        writerx.writerow(row_x_c);
        writery.writerow(row_y_c);

print('shape pf x:',pd.read_csv(filepath_x).shape);
print('shape pf y:',pd.read_csv(filepath_y).shape);
