#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    a = "Yes"
    b = "No"
    if n > m:
        print(b)
    else:
        d1 = defaultdict(int)
        for word in magazine:
            d1[word] += 1

        count = 1
        for word in note:
            if d1[word] == 0:
                count = 0
            else:
                d1[word] -= 1

        if count == 0:
            print(b)
        else:
            print(a)


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)