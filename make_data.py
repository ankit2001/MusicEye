

from imports import *


#Function to make data separating notes and cords and dumping them in a numy array
def make():
	output = []
	print("\n")
	notes_array = []
	for idx, file in enumerate(glob.glob("dataset/*.mid")):
		midi_file = converter.parse(file)
		parsing_notes = None
		print("Parsing file " + str(idx) + " > " + str(file))
		try:
			parser = instrument.partitionByInstrument(midi_file)
			parsing_notes =  parser.parts[0].recurse()
		except:
			parsing_notes = midi_file.flat.notes
		for el in parsing_notes:
			if isinstance(el, note.Note):
				notes_array.append(str(el.pitch))
			elif isinstance(el, chord.Chord):
				notes_array.append(".".join(str(x) for x in el.normalOrder))
	with open("notes_input", "wb") as filepath:
		pickle.dump(notes_array, filepath)
	total_diff_notes_classes = len(set(notes_array))
	print("\n")
	print("Total different output classes : " + str(total_diff_notes_classes))
	print("\n")
	print("Output array is :")
	print("\n")
	print(notes_array)
	output.append(notes_array)
	output.append(total_diff_notes_classes)
	return output
"""
# Testing purposes
if __name__ == "__main__":
	arr = make()
	print(arr)
"""


