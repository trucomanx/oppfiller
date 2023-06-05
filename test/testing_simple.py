#!/usr/bin/python

import sys
sys.path.append('../src');


import OppFiller.Filler as oppmg
import OppFiller.Functions as oppf
import numpy as np

row_data=np.array(
[670.79, 278.54, 672.53, 276.8 , 669.33, 276.84, 675.25, 277.91, 667.14, 277.75,
 678.84, 287.04, 662.72, 286.74, 682.33, 300.32, 656.31, 299.49, 678.67, 297.05,
 661.04, 296.6 , 673.59, 312.18, 663.08, 311.66, 671.87, 333.78, 661.95, 333.37,
 669.33, 353.9 , 658.41, 353.79]
);

row_x=oppf.drop_n_elements_randomly_in_row_data(row_data,8);

obj=oppmg.Filler(model_type='sequence1');

new_row=obj.FillRowData(row_x);

################################################################################
# showing

out=row_data.reshape((34,1));
out=np.append(out,  row_x.reshape((34,1)), axis=1);
out=np.append(out,new_row.reshape((34,1)), axis=1);
    
print(out)
