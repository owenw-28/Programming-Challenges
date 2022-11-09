from typing import Tuple

"""Gets the chord, given the root and color.

returns
    ----------
    chord : tuple
        the chord consisting of its notes -> (C, Eb, G), (F#, A, C#), ..

arguments
    ----------
    root : str
        the root note of the chord -> C, D, F#, Ab, ..
    color : str
        the color or type of chord -> m, M, dim, aug
"""
def chord_triad(root: str, color: str) -> Tuple:
    notes = ('C', 'D', 'E', 'F', 'G', 'A', 'B')
    shifts = ('bb', 'b', '', '#', 'x')

    def is_major(note):
        # checks if the third from the note is major
        # that's true for C, F, and G only        
        return note in (0, 3, 4)

    def third_note(note):
        return notes[(note + 2) % len(notes)]

    def minor(note, shift):
        shift -= is_major(note)
        return third_note(note) + shifts[shift]
    
    def major(note, shift):
        shift += not is_major(note)
        return third_note(note) + shifts[shift]

    triads = {
        'm' : (minor, major), 
        'M' : (major, minor),
        'dim': (minor, minor), 
        'aug': (major, major),
    }
    
    def get_note(root=root):
        note, shift = root[0], root[1:]
        return notes.index(note), shifts.index(shift)
    
    def get_interval(i, root=root):
        return triads[color][i](*get_note(root))
    
    third = get_interval(0)
    return (root, third, get_interval(1, third))

def main():
    root = input("Please enter root note of the chord: ")
    color = input("Please enter the type of chord: ")
    print(chord_triad(root, color))

main()



