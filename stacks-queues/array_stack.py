# Arjun Sabnis
# Array Stack Implementation
# Created on 9/12/2018

class ArrayStack(object):
    
    def __init__(self):
        self.array = []
        self.index = 0

    def create(self, length):
        self.array = [None]*length

    def is_empty(self):
        return (self.index == 0)

    def push(self, item):
        if (self.index == len(self.array)):
            self.resize(2*len(self.array))
        self.array[self.index] = item
        self.index += 1

    def pop(self):
        self.index -= 1
        item = self.array[self.index]
        self.array[self.index] = None
        if (self.index > 0 and self.index == (len(self.array)/4)):
            self.resize(len(self.array)/2)
        return item

    def resize(self, length):
        temp = [None]*length
        for i in range(self.index):
            temp[i] = self.array[i]
        self.array = temp

    def print_array(self):
        for i in range(len(self.array)):
            print self.array[i]
