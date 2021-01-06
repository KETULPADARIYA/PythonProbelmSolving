#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
from collections import  Counter


def pickingNumbers(a):
    # Write your code here
    counter_a = Counter(a)
    print(counter_a)
    return max( counter_a[k] +
                counter_a.get(k+1,0)
                for k in sorted(counter_a)
                )


if __name__ == '__main__':

    n = 6

    a = [ int(i) for i in "4 6 5 3 3 1".split()]


    result = pickingNumbers(a)

    print(result)