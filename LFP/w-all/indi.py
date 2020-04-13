from random import randint
from operator import add
from functools import reduce

def individual(length, min, max):
	return [randint(min,max) for x in range (length)]


def population(count, length, min, max):
	return [individual(length, min,max) for x in range (count)]

def fitness(individual, target):
    sum = reduce(add, individual, 0)
    return abs(target-sum)

def grade(pop, target):
    summed = reduce(add, (fitness(x, target) for x in pop), 0)
    return summed/ len((pop) * 1.0)
