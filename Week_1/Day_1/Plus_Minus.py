
import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Setting flags
    positive = 0
    negative = 0
    zero = 0
    
    # Looping and checking for number type
    for i in arr:
        if i > 0:
            positive =+ 1
        elif i < 0:
            negative =+ 1
        else:
            zero =+ 1
            
    print(str(round(positive/int(len(arr)),6))) 
    print(str(round(negative/int(len(arr)),6))) 
    print(str(round(zero/int(len(arr)),6))) 
            


n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

plusMinus(arr)
