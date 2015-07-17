from sticks import Computer

import random

proto = {}
end = [0 for _ in range(101)]

for i in range(101):
    proto[i] = [1, 2, 3]


class HardComputer(Computer):

    def __init__(self, name='Megatron'):
        super().__init__(name)
        self.start_hats = proto
        self.end_hats = end

    def reset(self):
        for i in range(101):
            self.end_hats[i] = 0

    def turn(self, sticks):
        num = random.choice(self.start_hats[sticks])

        while not 1 <= num <= 3 or not sticks - num >= 0:
            num = random.choice(self.start_hats[sticks])

        self.end_hats[sticks] = num
        return num

    def finish(self):
        for indx, val in enumerate(self.end_hats):
            if val is not 0:
                self.start_hats[indx].append(val)
