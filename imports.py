#importing all necessary files in it
from music21 import converter, note, chord, instrument, stream
import glob
import pickle
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM, Dropout, Activation
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint
