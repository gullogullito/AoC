"""
Author: Julio Pérez
Date: 01-12-2024
Description: Day 1 task 1 & 2 - Advent of Code 2024

"""

# Part 1
list1 = []
list2 = []

with open('./inputs/input1_1.txt', 'r') as f:
    for line in f:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))

differences = sum([abs(x - y) for x, y in zip(sorted(list1), sorted(list2))])

print("The sum of the differences between the two lists is: ", differences)

# Part 2
similarity_score = sum([x * list2.count(x) for x in list1])
print("The similarity score is: ", similarity_score)