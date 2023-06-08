#!/usr/bin/python

import os
import sys
import OppFiller.lib_models as opplb
import OppFiller.Functions as oppf
import numpy as np

class Filler:
    def __init__(self,model_type='sequence1'):
        checkpoint_path='';
        self.model_type=model_type;
        
        path_root = os.path.dirname(__file__);
        
        print('Loading model type:',self.model_type)
        
        if   self.model_type=='sequence1':
            checkpoint_path=os.path.join('models','model_sequence1','model.h5');
            path = os.path.join(path_root,checkpoint_path);
            self.modelo=opplb.create_model_sequence1(path);
            
        elif self.model_type=='sequence2':
            checkpoint_path=os.path.join('models','model_sequence2','model.h5');
            path = os.path.join(path_root,checkpoint_path);
            self.modelo=opplb.create_model_sequence2(path);
            
        else:
            raise TypeError("Unknown parameter model_type");
        
        print('\nModel',self.model_type,'loaded.\n');
    

    def FillRowData(self,data_row):
        return opplb.evaluate_model(self.modelo,data_row.reshape((1,34)));
        

    def FillPredictionData(self,Data,All=True):
        SHAPE=Data.shape;
        if SHAPE[0]!=17 or SHAPE[1]!=3:
            sys.exit('Data in FillPredictionData(Data) dont have shape (17,3), current shape'+str(SHAPE));
        
        row=np.zeros((1,34));
        
        # temporal vector and output matrix
        for lin in range(17):
                if Data[lin][2]>0:
                    row[0][2*lin+0]=Data[lin][0];
                    row[0][2*lin+1]=Data[lin][1];
        
        DataOut=Data.copy();
        
        #print(row)
        #print(Data)
        
        # Analizing
        if self.model_type=='sequence1':
            out=opplb.evaluate_model(self.modelo,row);
        else:
            row_c,xc,yc,S=oppf.normalize_valid_row_data(row);
            row_c_filled=opplb.evaluate_model(self.modelo,row_c);
            out=oppf.unnormalize_valid_row_data(row_c_filled,xc,yc,S);
        
        # Copying output vector
        for lin in range(17):
            if All or Data[lin][2]<=0.0:
                DataOut[lin][0]=out[0][2*lin+0];
                DataOut[lin][1]=out[0][2*lin+1];
                DataOut[lin][2]=1.0;
        
        return DataOut;
