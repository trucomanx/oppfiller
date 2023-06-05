#!/usr/bin/python

import os
import sys
import tensorflow as tf
import pathlib

def create_model_sequence1(file_of_weight=''):
    '''
    Retorna un modelo.
    Adicionalmente, si el archivo `file_of_weight` existe los pesos son cargados.
    
    :param file_of_weight: Archivo donde se encuentran los pesos.
    :type file_of_weight: str
    :return: Retorna un modelo de red neuronal
    :rtype: tensorflow.python.keras.engine.sequential.Sequential
    '''
    
    ninputs=34;
    noutputs=34;
    
    func=tf.keras.layers.LeakyReLU(alpha=0.01);
    
    # modelo nuevo
    model = tf.keras.models.Sequential();
    model.add(tf.keras.layers.Dense(       68, activation=func, input_shape=(ninputs, )) );
    model.add(tf.keras.layers.Dense(      102, activation=func) );
    model.add(tf.keras.layers.Dense(      136, activation=func) );
    model.add(tf.keras.layers.Dense(      102, activation=func) );
    model.add(tf.keras.layers.Dense(       68, activation=func) );
    model.add(tf.keras.layers.Dense( noutputs, activation=func) );
    
    if (len(file_of_weight)!=0):
        if pathlib.Path(file_of_weight).is_file():
            obj=model.load_weights(file_of_weight);
            print('\nThe file',file_of_weight,' was loaded\n')
        else:
            print('\nThe file',file_of_weight,'not exist, data not loaded\n')
    
    return model;


def create_model_sequence12(file_of_weight=''):
    '''
    Retorna un modelo.
    Adicionalmente, si el archivo `file_of_weight` existe los pesos son cargados.
    
    :param file_of_weight: Archivo donde se encuentran los pesos.
    :type file_of_weight: str
    :return: Retorna un modelo de red neuronal
    :rtype: tensorflow.python.keras.engine.sequential.Sequential
    '''
    
    ninputs=34;
    noutputs=34;
    
    func=tf.keras.layers.LeakyReLU(alpha=0.01);
    
    # modelo nuevo
    model = tf.keras.models.Sequential();
    model.add(tf.keras.layers.Dense(       68, activation=func, input_shape=(ninputs, )) );
    model.add(tf.keras.layers.Dense(      102, activation=func) );
    model.add(tf.keras.layers.Dense(      136, activation=func) );
    model.add(tf.keras.layers.Dense(      102, activation=func) );
    model.add(tf.keras.layers.Dense(       68, activation=func) );
    model.add(tf.keras.layers.Dense( noutputs, activation=func) );
    
    if (len(file_of_weight)!=0):
        if pathlib.Path(file_of_weight).is_file():
            obj=model.load_weights(file_of_weight);
            print('\nThe file',file_of_weight,' was loaded\n')
        else:
            print('\nThe file',file_of_weight,'not exist, data not loaded\n')
    
    return model;

def evaluate_model(model,data_row):
    return model.predict(data_row,verbose=0);

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_history(history,outdir='./',prename='training'):
    hist = pd.DataFrame(history.history)
    
    filepath=os.path.join(outdir,prename+'_history.csv');
    hist.to_csv(filepath,index=False);
    
    
    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('Mean Abs Error')
    plt.plot(history.epoch, np.array(hist['mae'])    , label = 'Train Error')
    plt.plot(history.epoch, np.array(hist['val_mae']), label = 'Val Error')
    #plt.ylim([0,5])
    plt.legend()
    filepath=os.path.join(outdir,prename+'_mae.svg');
    plt.savefig(filepath, dpi=150);
    
    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('Root Mean Square Error')
    plt.plot(history.epoch, np.sqrt(np.array(hist['mse']))    , label = 'Train Error')
    plt.plot(history.epoch, np.sqrt(np.array(hist['val_mse'])), label = 'Val Error')
    #plt.ylim([0,20])
    plt.legend()
    #plt.show()
    filepath=os.path.join(outdir,prename+'_rmse.svg');
    plt.savefig(filepath, dpi=150);
    

