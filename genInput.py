#!/bin/python

# Script to generate inputset for CS561 HW1. This is to judge average run time for high input sets

# For now, using inputs sans trees.
from random import randint
N = 1000
P = 7000
inputFile = open("input.txt", "w")
inputFile.write("DFS\n")
inputFile.write(str(N))
inputFile.write("\n")
inputFile.write(str(P))
genInput = [["0" for j in xrange(0, N)] for i in xrange(0, N)]

# Adding trees
T = 100000
for i in xrange(0, T):
    x = randint(0, N-1)
    y = randint(0, N-1)
    while genInput[x][y] == "2":
        x = randint(0, N - 1)
        y = randint(0, N - 1)
    genInput[x][y] = "2"

for i in xrange(0, N):
    inputFile.write("\n")
    inputFile.write("".join(genInput[i]))