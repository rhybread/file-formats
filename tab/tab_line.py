from tab.tuning import Tuning


class TabLine:
    def __init__(self, tuning: Tuning):
        # the total number of characters in the line, which will help to know where to put notes when and dashes when
        # converting from .tab to .txt
        self.line_length = 0
        self.tuning = tuning
        # each string has a list of Notes
        self.first, self.second, self.third, self.fourth, self.fifth, self.sixth = list()

    def add_note(self, string: str, index: int, note: str):
        # make sure the string is valid
        if not self.tuning.contains(string):
            return


