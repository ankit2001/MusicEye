

from imports import *

# Wrapper functtion to read the midi file
def read(file, head):

	# Uisng music21 to read midi file
	midi_file = converter.parse(file)
	parsing_notes = midi_file.flat.notes
	if len(parsing_notes) < head:
		head = len(parsing_notes)
	for el in parsing_notes[:head]:
		print(el, el.offset)

"""
#Testing sources 
if __name__ == "__main__":
	read("dataset/aguado-op03n02.mid", 20)
"""


