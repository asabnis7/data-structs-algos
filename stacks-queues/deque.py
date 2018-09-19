# Arjun Sabnis
# Deque implementation
# Created on 9/12/2018

class Deque(object):
    
    class _Node(object):
        
        def __init__(self):
            self.link = None
            self.item = None
    
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def is_empty(self):
        return (self.size == 0)

    def length(self):
        return(self.size)

    def add_front(self, item):
        old_front = self._Node()
        old_front = self.front
        self.front = self._Node()
        self.front.item = item
        self.front.link = old_front
        self.size += 1

    def add_back(self, item):
        old_back = self._Node()
        old_back = self.back
        self.back = self._Node()
        self.back.item = item
        self.back.link = old_back
        self.size += 1

    def remove_front(self):
        item = self.front.item
        self.front = self.front.link
        self.size -= 1
        return item

    def remove_back(self):
        item = self.back.item
        self.back = self.back.link
        self.size -= 1
        return item
