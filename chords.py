from midiutil import MIDIFile
from pprint import pprint
import inspect
import random


def name_the_file():
    filename = "example1.mid"
    return filename


def add_track(midi_file, name, track, tempo, program):
    time = 0
    midi_file.addTrackName(track, time, name)
    midi_file.addTempo(track, time, tempo)
    midi_file.addProgramChange(track, 0, 0, program)
    return midi_file


def add_note(note, midi_file, velocity, track, time, duration):
    print("note added")
    print(" note:" + str(note))
    print(" velocity:" + str(velocity))
    print(" track:" + str(track))
    print(" time:" + str(time))
    print(" duration:" + str(duration))
    midi_file.addNote(track, 0, note, time, duration, velocity)
    return midi_file


def add_chord(midi_file, track, time, duration, chord):
    print("chord start"+str(chord))
    for i in range(len(chord)):
        midi_file = add_note(chord[i], midi_file, 120, track, time, duration)
    print("chord end")
    return midi_file


def add_percussion_note(midi_file, track, instrument, time, duration):
    midi_file = add_note(instrument, midi_file, 120, track, time, duration)
    return midi_file


def add_multiple_percussion(midi_file):
    for i in range(20):
        midi_file = add_percussion_note(midi_file, 2, 36, i, 120)
    return midi_file


def add_bar_of_melody(midi_file, chord, rythmic_pattern, track, starting_time):
    for i in range(8):
        time = starting_time + i * 0.5
        add_note(random.choice(chord[i]) + 12, midi_file, rythmic_pattern[i], 1, time, 0.5)


def create_eight_bar_chord_progression(chords):
    eight_bar_prograssion = []
    odd_chords = (0, 2, 4)
    even_chords = (1, 3, 5)
    for i in range(8):
        choice = 0
        if i % 2 == 0:
            choice = random.choice(even_chords)
        else:
            choice = random.choice(odd_chords)
        eight_bar_prograssion.append(chords[choice])
        print(choice)
    return eight_bar_prograssion


def add_eight_bars_of_chords(midi_file, chords):
    for i in range(8):
        midi_file=add_chord(midi_file,0,i*4,4,chords[i])
    return midi_file


chords = [
    (55, 59, 62),
    (57, 60, 64),
    (59, 62, 66),
    (60, 64, 67),
    (62, 66, 69),
    (64, 67, 71)
]
rythmic_pattern = [100, 0, 80, 0, 80, 80, 80, 80]
# Create the MIDIFile object with one track
midi_file = MIDIFile(numTracks=5)
midi_file = add_track(midi_file, "chords", 0, 100, 48)
midi_file = add_track(midi_file, "melody", 1, 100, 42)
midi_file = add_track(midi_file, "drums", 2, 100, 35)

midi_file = add_multiple_percussion(midi_file)

progression=create_eight_bar_chord_progression(chords)

midi_file=add_eight_bars_of_chords(midi_file, progression)

for i in range(8):
    add_bar_of_melody(midi_file, progression, rythmic_pattern, 1, i * 4)

# Write the MIDI file to disk
with open(name_the_file(), "wb") as output_file:
    midi_file.writeFile(output_file)
