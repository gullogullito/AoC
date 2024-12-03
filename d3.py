"""
Author: Julio Pérez
Date: 03-12-2024
Description: Day 3 task 1 & 2 - Advent of Code 2024

"""

import re

def find_muls_sum(f):
    muls = ", ".join(re.findall(r"mul[(]\d+[,]\d+[)]", f))
    return sum([int(x)*int(y) for x, y in zip(re.findall(r"\d+", muls)[::2], re.findall(r"\d+", muls)[1::2])])

def find_muls_sum2(f):
    enabled = True
    sum2 = 0
    for dont, do, mul in re.findall(r"(don't[(][)])|(do[(][])])|mul[(](\d+[,]\d+)[)]", f):
        if mul:
            sum2 += int(mul.split(",")[0])*int(mul.split(",")[1]) if enabled else 0
        else:
            enabled = True if do else False      
    return sum2

final_sum = 0
final_sum2 = 0

with open('./inputs/input3.txt', 'r') as f:
    final_sum = find_muls_sum(f.read())
    f.seek(0)
    final_sum2 = find_muls_sum2(f.read())

    print("The sum of the mul orders is: ", final_sum)
    print("The sum of the enabled mul orders is: ", final_sum2)


