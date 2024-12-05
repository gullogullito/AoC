"""
Author: Julio Pérez
Date: 04-12-2024
Description: Day 4 task 1 & 2 - Advent of Code 2024

"""

import re

def getNeighbourhoodXMAS(matrix, x, y):

    surroundings= []
    z = x + 3
    t = y + 3
    if z >= 0 and t >= 0 and z < len(matrix) and t < len(matrix[0]):
        surroundings.append(matrix[x+1][y+1] + matrix[x+2][y+2] +  matrix[x+3][y+3])

    z = x - 3
    t = y - 3
    if z >= 0 and t >= 0 and z < len(matrix) and t < len(matrix[0]):
        surroundings.append(matrix[x-1][y-1] + matrix[x-2][y-2] +  matrix[x-3][y-3])

    z = x + 3
    t = y - 3
    if z >= 0 and t >= 0 and z < len(matrix) and t < len(matrix[0]):
        surroundings.append(matrix[x+1][y-1] + matrix[x+2][y-2] +  matrix[x+3][y-3])

    z = x - 3
    t = y + 3
    if z >= 0 and t >= 0 and z < len(matrix) and t < len(matrix[0]):
        surroundings.append(matrix[x-1][y+1] + matrix[x-2][y+2] +  matrix[x-3][y+3])

    z = x + 3
    t = y
    if z >= 0 and t >= 0 and z < len(matrix) and t < len(matrix[0]):
        surroundings.append(matrix[x+1][y] + matrix[x+2][y] +  matrix[x+3][y])
    
    z = x - 3
    t = y
    if z >= 0 and t >= 0 and z < len(matrix) and t < len(matrix[0]):
        surroundings.append(matrix[x-1][y] + matrix[x-2][y] +  matrix[x-3][y])
    
    z = x 
    t = y + 3
    if z >= 0 and t >= 0 and z < len(matrix) and t < len(matrix[0]):
        surroundings.append(matrix[x][y+1] + matrix[x][y+2] +  matrix[x][y+3])
    
    z = x 
    t = y - 3
    if z >= 0 and t >= 0 and z < len(matrix) and t < len(matrix[0]):
        surroundings.append(matrix[x][y-1] + matrix[x][y-2] +  matrix[x][y-3])

    return surroundings

def getNeighbourhoodMAS(matrix, x, y):
    xmas1 = []
    xmas2 = []
    neighbour = []

    z = x + 1
    t = y + 1
    if z >= 0 and t >= 0 and z < len(matrix) and t < len(matrix[0]):
        xmas1.append(matrix[z][t])
    
    z = x - 1
    t = y - 1
    if z >= 0 and t >= 0 and z < len(matrix) and t < len(matrix[0]):
        xmas1.append(matrix[z][t])
    
    xmas1 = ''.join(xmas1)

    z = x - 1
    t = y + 1
    if z >= 0 and t >= 0 and z < len(matrix) and t < len(matrix[0]):
        xmas2.append(matrix[z][t])
    
    z = x + 1
    t = y - 1
    if z >= 0 and t >= 0 and z < len(matrix) and t < len(matrix[0]):
        xmas2.append(matrix[z][t])
    
    xmas2 = ''.join(xmas2)
    neighbour.append(xmas1)
    neighbour.append(xmas2)

    return neighbour


def countXMAS(matrix):
    total = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'X':
                for chain in getNeighbourhoodXMAS(matrix,i,j):
                    if (re.findall(r"MAS", chain)):
                        total += 1                 
    return total

total_xmas = 0
total_xmas2 = 0

def countMAS(matrix):
    total = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'A':
                chain = getNeighbourhoodMAS(matrix,i,j)
                if ((chain[0] == 'MS' or chain[0] == 'SM') and (chain[1] == 'SM' or chain[1] == 'MS')):   
                    total += 1                 
    return total

with open('./inputs/input4.txt', 'r') as f:
    matrix = [list(x) for x in f]

    total_xmas += countXMAS(matrix)
    total_xmas2 += countMAS(matrix)

    print("The total number of XMAS is: ", total_xmas)
    print("The total number of MAS is: ", total_xmas2)