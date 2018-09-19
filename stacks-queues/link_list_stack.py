# Arjun Sabnis
# Linked Stack Implementation
# Created on 9/12/2018

class LinkStack(object):
    
    class _Node(object):
        
        def __init__(self):
            self.item = None
            self.next = None

   
    def __init__(self):
        self.first = None;

    def is_empty(self):
        return(self.first == None)

    def push(self, item):
        old = self._Node()
        old = self.first
        self.first = self._Node()
        self.first.item = item
        self.first.next = old

    def pop(self):
        item = self.first.item
        self.first = self.first.next
        return item
