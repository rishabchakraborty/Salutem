import cv2
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils
from keras import backend as K
K.set_image_dim_ordering('th')

# fix random seed for reproducibility
seed = 7
np.random.seed(seed)


import glob
from numpy import array
#USING PILL
from PIL import Image





filelist = glob.glob('ftrain/*.bmp')

X_train = []
for f1 in filelist:
    gray = cv2.imread(f1)
    img_gaussian = cv2.GaussianBlur(gray,(3,3),0)
    kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
    img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)
    X_train.append(img_prewittx + img_prewitty)


X_train = np.array(X_train)
X_train = X_train/255.0


#X_train = np.array([np.array(Image.open(fname)) for fname in filelist])

y_train = []

for i in xrange(0,11):
	y_train.append(i)
	y_train.append(i)
	

y_train = np.array(y_train)


filelist = glob.glob('ftest/*.bmp')

X_test = []
for f1 in filelist:
    gray = cv2.imread(f1)
    img_gaussian = cv2.GaussianBlur(gray,(3,3),0)
    kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
    img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)
    X_test.append(img_prewittx + img_prewitty)


X_test = np.array(X_test)
X_test = X_test/255.0

#X_test = np.array([np.array(Image.open(cv2.Canny(fname,50,100))) for fname in filelist])


y_test = []
for i in xrange(0,11):
	y_test.append(i)

y_test = np.array(y_test)



X_train = X_train.reshape(X_train.shape[0], 1, 90, 300).astype('float32') #last 3 arguments are input_shape
X_test = X_test.reshape(X_test.shape[0], 1, 90, 300).astype('float32')



y_train = np_utils.to_categorical(y_train).astype('int32') #This was commented earlier
y_test = np_utils.to_categorical(y_test).astype('int32')  #This was commented earlier



model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(1, 90, 300), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(15, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(50, activation='relu'))
model.add(Dense(20, activation='relu'))
model.add(Dense(11, activation='sigmoid'))


# Compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=15, batch_size=1)


# Final evaluation of the model
scores = model.evaluate(X_test, y_test, verbose=0)


print("Accuracy of CNN is: %.2f%%" % (scores[1]*100))


