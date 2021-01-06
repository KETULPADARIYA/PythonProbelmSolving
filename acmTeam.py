#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from itertools import combinations


# Complete the acmTeam function below.
def acmTeam(topic):
    # print("Hello WonderFul Persons.")
    print(topic)
    topic = [[int(integer) for integer in t] for t in topic]
    r = [sum(i or j for i, j in zip(p1, p2)) for p1, p2 in combinations(topic, 2)]
    max_3 = max(r)
    return max_3, Counter(r)[max_3]


def acmTeam1(topic):
    # print("Hello WonderFul Persons.")
    print(topic)
    topic = [int(t, 2) for t in topic]
    r = [bin(p1 | p2).count(1) for p1, p2 in combinations(topic, 2)]
    max_3 = max(r)
    return max_3, Counter(r)[max_3]


def acmTeam2(topic2):
    n = len(topic2)
    inp = topic2
    maxi = 0
    cnt = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            set_bit = bin(int(inp[i], 2) | (int(inp[j], 2))).count("1")
            print(set_bit)
            if set_bit > maxi:
                maxi = set_bit
                cnt = 1
            elif set_bit == maxi:
                cnt += 1
    return maxi, cnt


if __name__ == '__main__':
    1
