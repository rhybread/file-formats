from tab.tuning import Tuning
import re


class Chunk:
    def __init__(self, tuning: Tuning):
        self.tuning = tuning
        self.EMPTY_CHUNK = {
            tuning.first: list(),
            tuning.second: list(),
            tuning.third: list(),
            tuning.fourth: list(),
            tuning.fifth: list(),
            tuning.sixth: list()
        }
        self.current_chunk = self.EMPTY_CHUNK
        self.length = 0

    def is_full(self):
        return self.current_chunk.get(self.tuning.first) and \
               self.current_chunk.get(self.tuning.second) and \
               self.current_chunk.get(self.tuning.third) and \
               self.current_chunk.get(self.tuning.fourth) and \
               self.current_chunk.get(self.tuning.fifth) and \
               self.current_chunk.get(self.tuning.sixth)

    # todo: make sure all lines are the same length
    def chunk_length(self):
        return len(self.current_chunk.get(self.tuning.first))

    def add(self, line: str):
        notes = line.split('-')
        # short by the number of notes because it is excluding the dashes between them
        length = sum(len(note) if len(note) > 0 else 1 for note in notes)
        print(length)
        print(notes)

        # index = 0
        # for note in notes:
        #     if note == '':
        #         continue
        #
        #     if re.search("^[a-zA-Z]\|", note):
        #         continue
        #
        #     print((index, note))
        #
        #     length += 1
        #     note_length = len(note)
        #     index += note_length if note_length > 0 else 1
        #
        #
        # self.length = length # todo: throw error if doesn't match current length

