import numpy as np
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from PIL import Image
import PIL.ImageOps

X,y = fetch_openml('mnist_784',version=1,return_X_y=True)

X_train , X_test,y_train,y_test = train_test_split(X,y,random_state=9,train_size=7500,test_size=2500)

X_train_scale = X_train/255.0
X_test_scale = X_test/255.0

clf = LogisticRegression(solver='saga',multi_class='multinomial').fit(X_train_scale,y_train)

def getPrediction(img):
    f_open = Image.open(img)
    img_grayscale = f_open.convert('L')
    img_resize = img_grayscale.resize((28,28),Image.ANTIALIAS)
    pixel_filter = 20
    min_pixel = np.percentile(img_resize,pixel_filter)
    img_resize_invertedScale = np.clip(img_resize-min_pixel,0,255)
    max_pixel = np.max(img_resize)
    img_resize_invertedScale = np.asarray(img_resize_invertedScale)/max_pixel
    test_sample = np.array(img_resize_invertedScale).reshape(1,784)
    pred = clf.predict(test_sample)
    return pred[0]