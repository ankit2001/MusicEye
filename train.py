from imports import *
from make_data import make 
from preprocessing import network_params
from model import lstm_model


# Combining all the files to train the model 
notes = make()
arr = network_params(notes[0], notes[1], 100)
inputs = arr[0]
outputs = arr[1]
total_classes = notes[1]
model = lstm_model(inputs, total_classes)
print("\n")
print("Summary :")
print("\n")
print(model.summary())
weights = "trained.hdf5"
# if len(weights) > 0:
# 	model.load_weights(weights)

# Creating checkpoints to store weights after every iteration 
checkpoint = ModelCheckpoint("trained_model/{epoch:02d}-{loss:.4f}.h5", monitor = "loss", save_best_only = True, mode = "min", verbose = 1)
callbacks_list = [checkpoint]
model.fit(inputs, outputs, epochs = 100, batch_size = 64, callbacks = callbacks_list)

"""
call backs list for last model saved
"""