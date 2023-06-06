#!/usr/bin/python
import sys
import numpy as np
import random

def RotationMatrix(Angle=5):
    theta = (Angle/180.) * np.pi;
    
    #https://pt.wikipedia.org/wiki/Matriz_de_rota%C3%A7%C3%A3o
    RotMat = np.array([[ np.cos(theta),  np.sin(theta)], 
                       [-np.sin(theta),  np.cos(theta)]]);

    return RotMat;

def BigRotationMatrix(Angle=5):
    RotMat=RotationMatrix(Angle);
    
    Zeros=np.zeros((34,34));
    
    for n in range(17):
        Zeros[2*n:2*n+2,2*n:2*n+2]=RotMat.copy();

    return Zeros;
    

def check_data(data):
    if isinstance(data, list):
        if len(data)!=34:
            sys.exit("data is a list and don't have 34 elements. End of program");  
        data=np.array(data);
    
    if not isinstance(data, np.ndarray):
        sys.exit("data is not a list or numpy array. End of program");  
    
    if data.ndim==1:
        if data.size!=34:
            sys.exit("data is a numpy array and don't have 34 elements. End of program");
    elif data.ndim==2:
        if data.shape[1]!=34:
            sys.exit("data is a numpy array and don't have 34 columns. End of program");    
    else:
        sys.exit("data is a numpy array and don't have 1 or 2 dimensions. End of program");    
    
    return data;

def valid_center_of_row_data(row_data):
    if row_data.size!=34:
        sys.exit("The row don't have 34 elements");
    x0=0;
    y0=0;
    k=0;
    
    for n in range(17):
        if row_data[2*n]>0 and row_data[2*n+1]>0:
            x0=x0+row_data[2*n];
            y0=y0+row_data[2*n+1];
            k=k+1;
        else:
            print(row_data[2*n],row_data[2*n+1])
    
    return x0/k,y0/k;

def valid_rms_of_row_data(row_data):
    '''
    Calcula el valor root mean square de todas las cordenadas dos pontos em row_data.
    Desconsidera potos com ambos zeros.
    Acepta negativos.
    '''
    if row_data.size!=34:
        sys.exit("The row don't have 34 elements");
    S=0.0;
    k=0;
    
    for n in range(17):
        if row_data[2*n]!=0 or row_data[2*n+1]!=0:
            S=S+row_data[2*n]*row_data[2*n];
            S=S+row_data[2*n+1]*row_data[2*n+1];
            k=k+2;
        else:
            print(row_data[2*n],row_data[2*n+1])
    
    return np.sqrt(S/k);
    
def add_offset_to_valid_row_data(row_data,dx,dy):
    '''
    Agrega a todas las cordenadas em row_data.
    Desconsidera potos com ambos zeros.
    Acepta negativos.
    '''
    if row_data.size!=34:
        sys.exit("The row don't have 34 elements");
    
    row_data_new=np.zeros(row_data.shape);
    
    for n in range(17):
        if row_data[2*n]!=0 or row_data[2*n+1]!=0:
            row_data_new[2*n]  =dx+row_data[2*n];
            row_data_new[2*n+1]=dy+row_data[2*n+1];
    
    return row_data_new;

def add_offset_to_row_data(row_data,dx,dy):
    if row_data.size!=34:
        sys.exit("The row don't have 34 elements");
    
    row_data_new=np.zeros(row_data.shape);
    
    for n in range(17):
        row_data_new[2*n]  =dx+row_data[2*n];
        row_data_new[2*n+1]=dy+row_data[2*n+1];
    
    return row_data_new;

def multiply_value_to_valid_row_data(row_data,value):
    '''
    Multiplica a todas las cordenadas em row_data.
    Desconsidera potos com ambos zeros.
    Acepta negativos.
    '''
    if row_data.size!=34:
        sys.exit("The row don't have 34 elements");
    
    row_data_new=np.zeros(row_data.shape);
    
    for n in range(17):
        if row_data[2*n]!=0 or row_data[2*n+1]!=0:
            row_data_new[2*n]  =value*row_data[2*n];
            row_data_new[2*n+1]=value*row_data[2*n+1];
    
    return row_data_new;

def centering_rotation_of_row_data(row_data,angle):
    if row_data.size!=34:
        sys.exit("The row don't have 34 elements");
    
    
    xc,yc    = valid_center_of_row_data(row_data);
    
    new_row  = add_offset_to_row_data(row_data,-xc,-yc);
    
    RotMat   = BigRotationMatrix(angle);
    new_row  = new_row.reshape((34,1));
    out=np.matmul(RotMat,new_row);
    
    out = add_offset_to_row_data(out,+xc,+yc);
    
    out=out.reshape((34,));
    
    return out;
    
def RotateData(data,angle):
    data = check_data(data);
    
    RotMat=BigRotationMatrix(angle);
    
    if data.ndim==1:
        data=data.reshape((34,1));
        out=np.matmul(RotMat,data);
        
        out=out.reshape((34,));
    elif data.ndim==2:
        out=np.matmul(data,RotMat.T);
    
    return out;
    
def drop_n_elements_randomly_in_row_data(row_data,nholes):
    if row_data.size!=34:
        sys.exit("The row don't have 34 elements");
    
    out=row_data.copy();
    
    for i in range(nholes):
        pos=random.randint(0, 16);
        out[2*pos]=0;
        out[2*pos+1]=0;
    
    return out;

