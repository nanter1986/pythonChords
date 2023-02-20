from midiutil import MIDIFile
from pprint import pprint
import inspect


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


def add_chord(midi_file, track, time, duration, root, flavor):
    print("chord start")
    third = 4
    if flavor == "min":
        third = 3

    midi_file = add_note(root, midi_file, 120, track, time, duration)
    midi_file = add_note(root + third, midi_file, 120, track, time, duration)
    midi_file = add_note(root + 7, midi_file, 120, track, time, duration)
    print("chord end")
    return midi_file


def add_percussion_note(midi_file, track, instrument, time, duration):
    midi_file.addNote(instrument, midi_file, 120, track, time, duration)
    return midi_file


def add_multiple_percussion(midi_file):
    for i in range(20):
        midi_file = add_percussion_note(midi_file, 2, 36, i, 120)
        return midi_file


# Create the MIDIFile object with one track
midi_file = MIDIFile(numTracks=5)
midi_file = add_track(midi_file, "chords", 0, 100, 48)
midi_file = add_track(midi_file, "melody", 1, 100, 42)
midi_file = add_track(midi_file, "drums", 2, 100, 35)

midi_file = add_chord(midi_file, 0, 0, 4, 55, "maj")
midi_file = add_chord(midi_file, 0, 4, 4, 57, "min")
midi_file = add_chord(midi_file, 0, 8, 4, 59, "min")
midi_file = add_chord(midi_file, 0, 12, 4, 60, "maj")
midi_file = add_chord(midi_file, 0, 16, 4, 62, "maj")

midi_file = add_multiple_percussion(midi_file)

midi_file = add_note(62, midi_file, 100, 1, 0, 1)

# Write the MIDI file to disk
with open(name_the_file(), "wb") as output_file:
    midi_file.writeFile(output_file)
