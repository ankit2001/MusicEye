# Preprocessing 

from imports import *
from make_data import make

# Function to preprocess the inputs using dataset
def network_params(notes, total_classes, seq_len):
	output = []
	pitches = sorted(set(x for x in notes))
	mapping = dict((note, idx) for idx, note in enumerate(pitches))
	outputs = []
	inputs = []
	for idx in range(0, len(notes) - seq_len, 1):
		seq_out = notes[idx + seq_len]
		seq_in = notes[idx : idx + seq_len]
		outputs.append(mapping[seq_out])
		inputs.append([mapping[x] for x in seq_in])
	inputs = np.reshape(inputs, (len(inputs), seq_len, 1))
	output.append(inputs / float(total_classes))
	output.append(np_utils.to_categorical(outputs))
	output.append(inputs.shape)
	print("\n")
	print("Inputs are: ")
	print(output[0])
	print("\n")
	print("Outputs are: ")
	print("\n")
	print(output[1])
	print("\n")
	print("Shape of input layer > " + str(output[2]))
	return output
"""
#Testing purposes
if __name__ == "__main__":
	notes = make()
	arr = network_params(notes[0], notes[1], 100)
"""




