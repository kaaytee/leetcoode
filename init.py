#! /usr/bin/python3
import os

path = os.getcwd()

for i in range(1, 9):
    f = "/week" + str(i)
    os.mkdir(path + f)

