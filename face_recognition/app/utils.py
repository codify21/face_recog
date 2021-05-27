import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2 
from PIL import Image
from sklearn.decomposition import PCA
import pickle

#loading model
haar = cv2.CascadeClassifier('model/haarcascade_frontalface_default.xml')
#pickle files
mean = pickle.load(open('model/mean_preprocess.pickle','rb'))
model_svm = pickle.load(open('model/model_svm.pickle','rb'))
model_pca = pickle.load(open('model/pca_50.pickle','rb'))
# print ('Model Loaded Successfully')

 #settings
gender_pre = ['Male','Female']
font = cv2.FONT_HERSHEY_SIMPLEX


# # test data
# test_data_path = 'robert.jpg'
# color = 'bgr'
# # step-1: read image
# img = cv2.imread(test_data_path)
# def pipeline_model(img,color='rgb'):

def pipeline_model(path,filename,color='bgr'):
    #step1: read image in cv2
    img = cv2.imread(path)
    # step-2: convert into gray scale
    if color == 'bgr':
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    else:
        gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    # step-3: crop the face (using haar cascase classifier)
    faces = haar.detectMultiScale(gray,1.5,3)
    for x,y,w,h in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) # drawing rectangle
        roi = gray[y:y+h,x:x+w] # crop image
        # step - 4: normalization (0-1)
        roi = roi / 255.0
        # step-5: resize images (100,100)
        if roi.shape[1] > 100:
            roi_resize = cv2.resize(roi,(100,100),cv2.INTER_AREA)
        else:
            roi_resize = cv2.resize(roi,(100,100),cv2.INTER_CUBIC)
        # step-6: Flattening (1x10000)
        roi_reshape = roi_resize.reshape(1,10000) # 1,-1 can also be used
        # step-7: subtract with mean
        roi_mean = roi_reshape - mean
        # step -8: get eigen image
        eigen_image = model_pca.transform(roi_mean)
#          print(eigen_image)
        # step -9: pass to ml model (svm)
        results = model_svm.predict_proba(eigen_image)[0]
#         print (results)#[.21,.79]
        # step -10:
        predict = results.argmax() # 0 or 1 
        score = results[predict]
#         print(predict,score)
        # step -11:
        text = "%s : %0.2f"%(gender_pre[predict],score)
        cv2.putText(img,text,(x,y),font,1,(0,255,0),2)
    cv2.imwrite('static/predict/{}'.format(filename),img)
 

