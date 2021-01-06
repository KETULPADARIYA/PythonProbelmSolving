#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the viralAdvertising function below.
def viralAdvertising(n):
    total = 5
    total_like = 0
    for i in range(n):
        like = int(total/2)
        total_like += like
        total = like * 3
    return total_like


if __name__ == '__main__':
    n = int(input())
    result = viralAdvertising(n)
    print(result)