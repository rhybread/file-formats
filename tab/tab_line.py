from tab.tuning import Tuning


class TabLine:
    def __init__(self, tuning: Tuning):
        self.line_length = 0
        self.tuning = tuning
        self.first, self.second, self.third, self.fourth, self.fifth, self.sixth = list()

    def add_note(self, string: str, index: int, note: str):
        print()
