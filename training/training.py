#!/usr/bin/python

import os
import sys
sys.path.append('../src');

import OppFiller.lib_models as opplm
import tensorflow as tf
import pandas as pd
import csv

################################################################################

BATCHSIZE=32;
EPOCHS=150;
model_type='sequence1';
dataset_x_path='../dataset/2-data/data_x.csv';
dataset_y_path='../dataset/2-data/data_y.csv';

################################################################################

X=pd.read_csv(dataset_x_path).copy();
Y=pd.read_csv(dataset_y_path).copy();



from sklearn.model_selection import train_test_split
X_train_full, X_test, Y_train_full, Y_test = train_test_split(           X,            Y,  test_size=0.25,shuffle=True)
X_train, X_valid, Y_train, Y_valid         = train_test_split(X_train_full, Y_train_full, train_size=0.70,shuffle=True)

print('\n')
print('X_train.shape:',X_train.shape,'Y_train.shape:',Y_train.shape)
print('X_valid.shape:',X_valid.shape,'Y_valid.shape:',Y_valid.shape)
print(' X_test.shape:',X_test.shape ,' Y_test.shape:',Y_test.shape)
print('\n')


if   model_type=='sequence1':
    model= opplm.create_model_sequence1();
elif model_type=='sequence2':
    model= opplm.create_model_sequence2();
else:
    raise TypeError("Unknown parameter model_type");

model.summary()
model.compile(optimizer='adam', 
              loss='mse',
              metrics=['mae', 'mse'])


output_dir='model_'+model_type;
os.makedirs(output_dir,exist_ok=True) 
print(output_dir)


best_model_file=os.path.join(output_dir,'model.h5');
checkpoint = tf.keras.callbacks.ModelCheckpoint(filepath=best_model_file, 
                                                save_weights_only=True,
                                                monitor='mse', 
                                                save_best_only=True, 
                                                verbose=1);

hist = model.fit(X_train, Y_train,
                 batch_size=BATCHSIZE,
                 epochs=EPOCHS,
                 validation_data=(X_valid, Y_valid),
                 callbacks=[checkpoint],
                 verbose=True);

opplm.plot_history(hist,outdir=output_dir,prename='training')

print('\nEvaluate:')
model.load_weights(best_model_file);
results = model.evaluate(X_test, Y_test)
results = dict(zip(model.metrics_names,results));
csv_filepath=os.path.join(output_dir,'test_evaluate.csv');
with open(csv_filepath, 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in results.items():
       writer.writerow([key, value])






