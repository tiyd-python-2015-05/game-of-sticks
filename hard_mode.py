from sticks import Computer

import random

proto = {}
end = {}
for i in range(101):
    proto[i] = [1,2,3]
    end[i] = []

class HardComputer(Computer):

    def __init__(self,name='Megatron'):
        super().__init__(name)
        self.start_hats = proto
        self.end_hats = end

    def reset(self):
        self.end_hats = end

    def turn(self, sticks):
        num = random.choice(self.start_hats[sticks])
        while not (1 <= num <= 3 and sticks - num >= 0):
            num = random.choice(self.start_hats[sticks])

        self.end_hats[sticks].append(num)
        return num

    def finish(self):
        for key, val in self.end_hats.items():
            if val is not []:
                self.start_hats[key].append(val)
                self.start_hats[key].append(val)
