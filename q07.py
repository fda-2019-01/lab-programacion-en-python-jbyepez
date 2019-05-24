##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras de la primera columna que aparecen
## asociadas a dicho valor de la segunda columna. Esto es:
##
##    ('0', ['C'])
##    ('1', ['E', 'B', 'D', 'A', 'A', 'E'])
##    ('2', ['A', 'E', 'D'])
##    ('3', ['A', 'B', 'D', 'E', 'E'])
##    ('4', ['E', 'B'])
##    ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
##    ('6', ['C', 'E', 'A', 'B'])
##    ('7', ['A', 'C', 'E', 'D'])
##    ('8', ['E', 'E', 'A', 'B'])
##    ('9', ['A', 'B', 'E', 'C'])
##
##
import itertools
from operator import itemgetter

csv = open('data.csv','r').readlines()
csv = [line[:-1] for line in csv]
csv = [line.split('\t') for line in csv]

list = []
for key, group in itertools.groupby(sorted([[row[1], row[0]] for row in csv], key=itemgetter(0)),itemgetter(0)):
    values = [line[1] for line in group]
    list.append((key,values))

for row in list:
    print(row)