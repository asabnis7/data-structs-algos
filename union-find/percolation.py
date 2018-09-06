# Arjun Sabnis
# Percolation simulator
# Created on 9/6/2018

import numpy
import union_find
from random import randint 


class Percolation(object):


    def __init__(self, size):
        self.grid = numpy.zeros((size,size))
        # self.grid = [[0 for i in range(size)] for i in range(size)]
        self.open_sites = 0.0;
        self.index = union_find.UnionFind(size*size)
        self.size = size
        self.percolate = False


    def is_open(self, row, col):
        if (row >= 0 and col >= 0 and row < self.size and col < self.size):
            if (self.grid[row][col] == 1):
                return True
            else:
                return False
        else:
            return False


    def is_full(self, row, col):
        if (row >= 0 and col >= 0 and row < self.size and col < self.size):
            if (self.grid[row][col] == 0):
                return True
            else:
                return False
        else: 
            return False


    def num_open_sites(self):
        return self.open_sites


    def open(self, row, col):
        if (row >= 0 and col >= 0 and row < self.size and col < self.size):
            if self.is_full(row, col) == True:
                self.grid[row][col] = 1
                self.open_sites += 1.0
            else:
                pass
            
            list_ind = row*self.size + col
            if (col > 0):
                if self.is_open(row, col-1) and not(self.index.connected(list_ind, list_ind-1)):
                    self.index.union(list_ind, list_ind-1)
                    # print "pass col-1"
            if (row > 0):
                if self.is_open(row-1, col) and not(self.index.connected(list_ind, (row-1)*self.size+col)):
                    self.index.union(list_ind, (row-1)*self.size+col)
                    # print "pass row-1"
            if (col < self.size-1):
                if self.is_open(row, col+1) and not(self.index.connected(list_ind, list_ind+1)):
                    self.index.union(list_ind, list_ind+1)
                    # print "pass col+1"
            if (row < self.size-1):
                if self.is_open(row+1, col) and not(self.index.connected(list_ind, (row+1)*self.size+col)):
                    self.index.union(list_ind, (row+1)*self.size+col)
                    # print "pass row+1"


    def percolates(self):
        for i in range(self.size):
            for j in range(self.size):
                if (self.index.connected(i, (self.size-1)*self.size+j) == True):
                    self.percolate = True
                    

    def print_array(self):
        self.index.print_nodes()
        for i in range(self.size):
            print "[",
            for j in range(self.size):
                print self.grid[i][j],
            print "]"


    def threshold(self):
        while not(self.percolate):
            rand_row = randint(0, self.size-1)
            rand_col = randint(0, self.size-1)

            self.open(rand_row, rand_col)
            self.percolates()

            # p1.print_array()

        return self.open_sites/float(self.size*self.size)
        #open_sites = p1.num_open_sites()
        #total_sites = float(size*size)
        #print "Percolation threshold: %f" % (open_sites/total_sites)
