import numpy as np
import random
from random import randint

# selection sort
def selection_sort(values):
    for i in range(len(values)):
        ind = np.argmin(values[i:])
        values[i], values[ind+i] = values[ind+i], values[i]

# insertion sort
def insertion_sort(values):
     for i in range(len(values)):
         for j in range(i, 0, -1):
             if (values[j] < values[j-1]):
                 values[j], values[j-1] = values[j-1], values[j]

# shell sort
def shell_sort(values):
    h = 1
    while (h < len(values)/3): 
        h = 3*h+1 # 3x+1 increments 
    while (h > 0):
        for i in range(h, len(values)):
            for j in range(i, h-1, -h):
              if (values[j] < values[j-h]):
                 values[j], values[j-h] = values[j-h], values[j]
        h = h/3;

# shuffle
def shuffle(values):
    for i in range(len(values)):
        r = randint(0,i)
        values[i], values[r] = values[r], values[i]



values = random.sample(xrange(1000),20)
print values
#selection_sort(values)
#insertion_sort(values)
shell_sort(values)
print values
#shuffle(values)
#print values
