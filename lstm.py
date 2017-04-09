from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding,BatchNormalization
from keras.layers import LSTM
from keras.optimizers import rmsprop,adadelta

dim_feature=150
timestep=10

model = Sequential()
#model.add(Embedding(20000, 256, input_length=80))
#model.add(Convolution2D(4,5, 5, border_mode='valid',input_shape=(3,240,320))) 
#model.add(Flatten())
model.add(LSTM(output_dim=512,return_sequences=False,input_shape=(timestep,dim_feature)))
model.add(Dropout(0.2))
model.add(LSTM(512, return_sequences=False))
model.add(Dropout(0.2))
#model.add(Dense(1024,activation='relu'))
#model.add(Dropout(0.5))
#model.add(Dense(512,activation='relu'))
#model.add(Dropout(0.5))
model.add(Dense(51))
model.add(Activation('softmax'))

#model.load_weights('my_weights/ucf101_train_lstm1000_001_19.h5')

for layer in model.layers:
    layer.trainable=True 

Rmsprop=rmsprop(lr=0.001)
Adadelta=adadelta(lr=0.001)
model.compile(loss='categorical_crossentropy',#'binary_crossentropy',
              optimizer=Rmsprop,
              metrics=['accuracy'])