#!/usr/bin/python

import os
import OppFiller.lib_models as opplb

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
