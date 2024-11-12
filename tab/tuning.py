class Tuning:
    def __init__(self, first: str, second: str, third: str, fourth: str, fifth: str, sixth: str):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth
        self.fifth = fifth
        self.sixth = sixth

    def contains(self, char: str):
        return self.first == char or self.second == char or self.third == char \
            or self.fourth == char or self.fifth == char or self.sixth == char
