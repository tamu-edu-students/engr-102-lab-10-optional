# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         YOUR NAME
# Section:      YOUR SECTION NUMBER
# Assignment:   THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date:         DAY MONTH YEAR

from time import time

def list_nums(n):
    '''chatgpt solution'''
    for a in range(1, n):
        for b in range(a, n):
            for c in range(b, n):
                for d in range(c, n):
                    if a**2 + b**2 + c**2 + d**2 == n:
                        return [a, b, c, d]

# how to measure how long your function takes to run:
t1 = time() # get start time
print(list_nums(15)) # run function
t2 = time() # get end time
print(f"This took {t2-t1} seconds") # print result