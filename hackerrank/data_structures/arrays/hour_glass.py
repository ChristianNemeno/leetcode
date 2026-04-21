#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
# [0][0]
def hourglassSum(arr):
    # Write your code here
    total = 0
    maximum = -float('inf')
    for i in range(4):
        for j in range(4):
            # The hour glass
            total = arr[0+i][0+j] + arr[0+i][1+j] + arr[0+i][2+j] + arr[1+i][1+j]+arr[2+i][0+j]+ arr[2+i][1+j] + arr[2+i][2+j]
            
            if maximum < total: 
                maximum = total
    
    return maximum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
