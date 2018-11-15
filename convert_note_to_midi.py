"""
Note to MIDI Number converter

Author: Kevin Jiang
Disclaimer: this probably already exists but YOLO
"""

import sys, os.path

# Constants
NOTES = ['C','D','E','F','G','A','B'] 
ACCIDENTALS = ['b', ''] # Flat and Natural (sharps are for plebs)
NON_ACCIDENTAL_NOTES = ['F', 'C'] # F and C are not usually referred to as E# and B# (unless ur a pleb)

# Returns mapping from notes (i.e. C6, G9, A0) to MIDI indexes
def generate_mapping():
	# Notes C0 to Ab0 will probably never be indexed, but generated for convenience
	midi_idx = 12 
	res = {}

	for octave in range(10):
		for note in NOTES:
			if note not in NON_ACCIDENTAL_NOTES:
				for accidental in ACCIDENTALS:
					curr = note + accidental + str(octave)
					res[curr] = midi_idx
					midi_idx += 1
			else: # F or C
				curr = note + str(octave)
				res[curr] = midi_idx
				midi_idx += 1

	return res

if __name__ == "__main__":
	input_notes = sys.argv[1:]

	if os.path.isfile("note2midi_map"):
		with open("note2midi_map", 'r') as f:
			mapping = eval(f.read())
	else:
		with open("note2midi_map", 'w') as f:
			mapping = generate_mapping()
			f.write(str(mapping))
		
	res = []

	for note in input_notes:
		res.append(mapping[note])

	print(res)
