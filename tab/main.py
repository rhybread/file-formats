import re

from tab.tuning import Tuning
from tab.note import Note


class Tab:
    def __init__(self):
        self.tuning = Tuning('e', 'B', 'G', 'D', 'A', 'E')
        self.current_string = ''

    def make_tab(self, txt):
        for line in txt:
            # if the line is not a line of tablature, such as lyrics, etc. just skip the line
            if not re.match("^[a-zA-Z]\|", line):
                continue
            self.__read_line(line)

    def __read_line(self, line: str):
        # get all the notes that are played in a list
        # when we get to a new note, we can just pop one out of this list because we know it's the next note in the line
        notes = line.split('-')
        # todo: get rid of ''
        # todo: get rid of start and end '|' characters
        print(notes)

        for index, char in enumerate(line):
            # if the character is a dash we just ignore it
            if char == '-':
                continue

            # if the character is just one of the letters denoting the string, we don't want to count it as a note
            if self.tuning.contains(char):
                continue

            # make a Note with the next string of characters
            current_note = notes.pop(0) # shouldn't need to worry about checking len > 0 because it should always align
            note = Note(index, current_note)


def main():
    txt = open("txts/like_real_people_do.txt", "r")
    tab = Tab()
    tab.make_tab(txt)
    txt.close()
    return


if __name__ == '__main__':
    main()

'''
** thoughts ** 

- need to deal with keeping the indices of the notes the same across the six strings for a given row
    - check for a newline at the end of the sixth string line
'''