# Model file

from imports import *
from preprocessing import network_params
from make_data import make
from keras.layers import BatchNormalization as BatchNorm
#Function to create lstm model for training 
def  lstm_model(inputs, total_classes):
	model = Sequential()
	model.add(LSTM(
		512,
		#input_shape=(inputs.shape[1], inputs.shape[2]),
		input_shape=(inputs.shape[1], inputs.shape[2]),
		recurrent_dropout=0.3,
		return_sequences=True
	))
	model.add(LSTM(512, return_sequences=True, recurrent_dropout=0.3,))
	model.add(LSTM(512))
	model.add(BatchNorm())
	model.add(Dropout(0.3))
	model.add(Dense(256))
	model.add(Activation('relu'))
	model.add(BatchNorm())
	model.add(Dropout(0.3))
	model.add(Dense(total_classes))
	model.add(Activation('softmax'))
	model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
	return model


#Testing purposes
if __name__ == "__main__":
	notes = make()
	arr = network_params(notes[0], notes[1], 100)
	inputs = arr[0]
	total_classes = notes[1]
	model = lstm_model(inputs, total_classes)
