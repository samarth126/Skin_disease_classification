import os
import matplotlib.pyplot as plt
import tensorflow as tf
import keras
import cv2
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import Input, Convolution2D, ZeroPadding2D,MaxPooling2D, Flatten, Dense, Dropout, Activation
from PIL import Image
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, save_img, img_to_array
from tensorflow.keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras.preprocessing import image
import pandas as pd
import pickle 
import joblib
from tensorflow.keras.applications import  VGG19
from tensorflow.keras.models import Model
from keras.applications.vgg19 import preprocess_input


train_list_mod=['Acne and Rosacea Photos', 'Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions', 'Atopic Dermatitis Photos', 'Eczema Photos', 'Nail Fungus and other Nail Disease', 'Psoriasis pictures Lichen Planus and related diseases']

# def data_dictionary():
#     path_train="./train/"
#     path_test="./test/"
#     list_train=train_list_mod#os.listdir(path_train)
#     train_dictionary={"image_path":[],"target":[]}
#     test_dictionary={"image_path":[],"target":[]}
#     k=0
#     for i in list_train:
#         path_disease_train=path_train+i
#         path_disease_test=path_test+i
#         image_list_train=os.listdir(path_disease_train)
#         image_list_test=os.listdir(path_disease_test)
#         for j in image_list_train:
#             img_path_train=path_disease_train+"/"+j
#             train_dictionary["image_path"].append(img_path_train)
#             train_dictionary['target'].append(k) 
#         for m in image_list_test :
#             img_path_test=path_disease_test+"/"+m
#             test_dictionary["image_path"].append(img_path_test)
#             test_dictionary['target'].append(k)
#         k+=1 
#     test_df=pd.DataFrame(test_dictionary)
#     train_df=pd.DataFrame(train_dictionary)
        
#     return  train_df,test_df

# def load_data(input_size=(100,100)):
#     images=[]
#     images2=[]
#     train_df,test_df=data_dictionary()
#     for i in train_df['image_path']:
#         img=cv2.imread(i)
#         img=cv2.resize(img,input_size)
#         images.append(img)
#     y_train=np.asarray(train_df['target'])
#     x_train=np.asarray(images)
#     for i in test_df['image_path']:
#         img=cv2.imread(i)
#         img=cv2.resize(img,input_size)
#         images2.append(img)
#     y_test=np.asarray(test_df['target'])
#     x_test=np.asarray(images2)
#     return x_train,x_test,y_train,y_test


vgg16 = VGG19(include_top=False,weights='imagenet')
# vgg16=joblib.load("./vgg16.sav")

new=os.listdir('./test') 
# print(new)

# x_train,x_test,y_train,y_test=load_data(input_size=(100,100))

# train_img=preprocess_input(x_train)
# test_img=preprocess_input(x_test)


# features_train=vgg16.predict(train_img)
# features_test=vgg16.predict(test_img)

def load_img(img_path):
    images=[]
    img=cv2.imread(img_path)
    # print(img)
    img=cv2.resize(img,(100,100))
    images.append(img)
    x_test=np.asarray(images)
    test_img=preprocess_input(x_test)
    features_test=vgg16.predict(test_img)
    num_test=x_test.shape[0]
    f_img=features_test.reshape(num_test,4608)
    
    return f_img


new_model = tf.keras.models.load_model('./saved_model/skin_model/')

img=load_img("./test/Eczema Photos/03DermatitisLeg.jpg")

q=np.argmax(new_model.predict(img))
print(q)

# Check its architecture
# x=new_model.summary()
# print(x)

