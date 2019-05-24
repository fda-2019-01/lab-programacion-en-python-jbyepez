##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras (ordenadas) de la primera 
## columna que aparecen asociadas a dicho valor de la segunda 
## columna. Esto es:
##
## ('0', ['C'])
## ('1', ['A', 'A', 'B', 'D', 'E', 'E'])
## ('2', ['A', 'D', 'E'])
## ('3', ['A', 'B', 'D', 'E', 'E'])
## ('4', ['B', 'E'])
## ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
## ('6', ['A', 'B', 'C', 'E'])
## ('7', ['A', 'C', 'D', 'E'])
## ('8', ['A', 'B', 'E', 'E'])
## ('9', ['A', 'B', 'C', 'E'])
##
##
import itertools
from operator import itemgetter

csv = open('data.csv','r').readlines()
csv = [line[:-1] for line in csv]
csv = [line.split('\t') for line in csv]

list = []
for key, group in itertools.groupby(sorted([[row[1], row[0]] for row in csv]),itemgetter(0)):
    values = [line[1] for line in group]
    list.append((key,values))

for row in list:
    print(row)