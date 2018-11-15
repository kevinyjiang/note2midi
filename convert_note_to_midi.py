"""
Note to MIDI Number converter

Author: Kevin Jiang
Disclaimer: this probably already exists but YOLO

"""

import sys

# Constants
NOTES = ['C','D','E','F','G','A','B']
ACCIDENTALS = ['b', '']
NON_ACCIDENTAL_NOTES = ['F', 'C']

# Returns mapping from notes (i.e. C6) to MIDI indexes
def generate_mapping():
	midi_idx = 12
	note_to_midi_dict = {}

	for octave in range(10):
		for note in NOTES:
			if note not in NON_ACCIDENTAL_NOTES:
				for accidental in ACCIDENTALS:
					curr = note + accidental + str(octave)
					note_to_midi_dict[curr] = midi_idx
					midi_idx += 1
			else: # F or C
				curr = note + str(octave)
				note_to_midi_dict[curr] = midi_idx
				midi_idx += 1

	return note_to_midi_dict

if __name__ == "__main__":
	input_notes = sys.argv[1:]
	mapping = generate_mapping()

	res = []

	for note in input_notes:
		res.append(mapping[note])

	print(res)
