"""
Author: Julio Pérez
Date: 01-12-2024
Description: Day 2 task 1 & 2 - Advent of Code 2024

"""

def safe(report: list):
    inc = all(i < j for i, j in zip(report, report[1:]))
    dec = all(i > j for i, j in zip(report, report[1:]))

    dif = all(abs(i - j) <= 3 and abs(i - j) >= 1 for i, j in zip(report, report[1:]))

    return (inc or dec) and dif

def safe2(report: list):
    if (safe(report)):
        return True
    else:
        for i in range(len(report)):
            removeSingleLevel = report.copy()
            removeSingleLevel.pop(i)
            if safe(removeSingleLevel):
                return True
    return False

total_safe = 0
total_safe2 = 0

with open('./inputs/input2.txt', 'r') as f:
    for line in f:
        report = [int(x) for x in line.split()]
        total_safe += 1 if safe(report) else 0
        total_safe2 += 1 if safe2(report) else 0

print("The total number of safe reports is: ", total_safe)
print("The total number of safe reports using the Problem Dampener is: ", total_safe2)