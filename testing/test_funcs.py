#!/usr/bin/python

import sys
sys.path.append('../src');


import OppFiller.Functions as oppf
import OppFiller.Filler as oppmg
import OppFiller.lib_models as opplm
import numpy as np

data=np.array(range(34))
data=data.reshape((1,34))

out=oppf.RotateData(data,-180);

print(data)
print(out)


filler=oppmg.Filler(model_type='sequence1');

model= opplm.create_model_sequence1();
model.summary()


