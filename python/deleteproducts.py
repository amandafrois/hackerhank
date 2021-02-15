#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'deleteProducts' function below.

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ids
#  2. INTEGER m

from numpy import array

def deleteProducts(ids,m):

# Creating an empty dictionary

    freq = {} #to count frequency of ids
    for item in ids:
        if (item in freq): 
            freq[item] += 1
        else:
            freq[item] = 1

    sortedfreq = sorted(freq.items(), key=lambda x: x[1], reverse=False)
    uniqueids=len(sortedfreq)
    delete=0

    for i in sortedfreq:
        if i[1]<=m:
            delete=delete+1
            m=m-i[1]
        else:
            break
    return uniqueids-delete



# Driver function 
if __name__ == "__main__": 
	my_list =array([1, 1, 1, 2, 3, 2])
	m=2
	print(deleteProducts(my_list,m)) 