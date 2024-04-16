from collections import deque

class FreqStack:
    def __init__(self):
        self.freq_dct = {}
        self.stack = deque()

    def push(self, val: int) -> None:
        if val not in self.freq_dct:
            self.freq_dct[val] = 0
        self.freq_dct[val] += 1
        frequency = self.freq_dct[val]
        if len(self.stack) < frequency:
            self.stack.append(deque())
        self.stack[frequency - 1].append(val)

    def pop(self) -> int:
        max_frequency = len(self.stack)
        val = self.stack[max_frequency - 1].pop()
        self.freq_dct[val] -= 1
        if not self.stack[max_frequency - 1]:
            self.stack.pop()
        return val
