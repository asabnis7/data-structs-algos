# Arjun Sabnis
# Union Find Algorithm
# Created on 9/6/2018

class UnionFind(object):
    
    def __init__(self, length):
        self.id = []
        self.length = length
        self.size = []

        for i in range(length):
            self.id.append(i)
            self.size.append(1)

    def root(self, index):
        while (index != self.id[index]):
            self.id[index] = self.id[self.id[index]]
            index = self.id[index]
        return index

    def connected(self, node1, node2):
        return self.root(node1) == self.root(node2)

    def union(self, node1, node2):
        i = self.root(node1)
        j = self.root(node2)
        
        if (i == j): 
            return
        
        if (self.size[i] < self.size[j]):
            self.id[i] = self.id[j]
            self.size[j] += self.size[i]
        else:
            self.id[j] = self.id[i]
            self.size[i] += self.size[j]
    
    def print_nodes(self):
        print "[",
        for i in range(self.length):
            print "%r " % self.id[i],
        print "]"
        
    #    print "[",
    #    for i in range(self.length):
    #        print "%r " % self.size[i],
    #    print "]"

