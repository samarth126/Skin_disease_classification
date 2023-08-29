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



# new=os.listdir('./test') 

def get_class(img_1):

    vgg16 = VGG19(include_top=False,weights='imagenet')

    def load_img(img):
        images=[]
        # img=cv2.imread(img_path)
        # print(img)
        img=cv2.resize(img,(100,100))
        images.append(img)
        x_test=np.asarray(images)
        test_img=preprocess_input(x_test)
        features_test=vgg16.predict(test_img)
        num_test=x_test.shape[0]
        f_img=features_test.reshape(num_test,4608)
        
        return f_img


    new_model = tf.keras.models.load_model('./skin_disease/saved_model/skin_model/')

    img=load_img(img_1)

    q=np.argmax(new_model.predict(img))
    return q


