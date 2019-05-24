##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
import itertools
from operator import itemgetter

csv = open('data.csv','r').readlines()
csv = [line[:-1] for line in csv]
csv = [line.split('\t') for line in csv]

for key, group in itertools.groupby(sorted(csv),itemgetter(0)):
    values = [int(line[1]) for line in group]
    print(key+','+str(max(values))+','+str(min(values)))