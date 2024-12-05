"""
Author: Julio Pérez
Date: 05-12-2024
Description: Day 5 task 1 & 2 - Advent of Code 2024

"""

total_sum, total_sum2 = 0,0
before_dependecies = []
after_dependencies = []
dependencies = []
updates = []

def isCorrectReturnMiddle(before, after, dependencies, pages):
    for page in pages:
        if page in before:
            for x in pages[pages.index(page)+1:]:
                dep = page + '|' + x
                if dep not in dependencies:
                    return 0

    return int(pages[len(pages)//2])

def orderIncorrectReturnMiddle(before, after, dependencies, pages):
    if isCorrectReturnMiddle(before, after, dependencies, pages) != 0:
        return 0
    correct_pages = pages.copy()

    for i in range(len(correct_pages)-1):
        for j in range(i+1, len(correct_pages)):
            dep = correct_pages[i] + '|' + correct_pages[j]
            if dep in dependencies:
                correct_pages[i], correct_pages[j] = correct_pages[j], correct_pages[i]
    
    return int(correct_pages[len(correct_pages)//2])



with open('./inputs/input5.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if "|" in line:
            dependencies.append(line)
            before_dependecies.append(line.split('|')[0])
            after_dependencies.append(line.split('|')[1])
        elif "," in line:
            updates.append(list(line.split(',')))
    
    total_sum = sum([isCorrectReturnMiddle(before_dependecies, after_dependencies, dependencies, update) for update in updates])
    total_sum2 = sum([orderIncorrectReturnMiddle(before_dependecies, after_dependencies, dependencies, update) for update in updates])

    print("Total sum of middle pages in correct order updates: ", total_sum)
    print("Total sum of middle pages in incorrect order updates: ", total_sum2)
