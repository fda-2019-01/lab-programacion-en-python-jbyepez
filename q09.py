##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras (ordenadas y sin repetir letra) 
## de la primera  columna que aparecen asociadas a dicho valor de la 
## segunda columna. Esto es:
##
## ('0', ['C'])
## ('1', ['A', 'B', 'D', 'E'])
## ('2', ['A', 'D', 'E'])
## ('3', ['A', 'B', 'D', 'E'])
## ('4', ['B', 'E'])
## ('5', ['B', 'C', 'D', 'E'])
## ('6', ['A', 'B', 'C', 'E'])
## ('7', ['A', 'C', 'D', 'E'])
## ('8', ['A', 'B', 'E'])
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
    values = sorted(set([line[1] for line in group]))
    list.append((key,[value for value in values]))

for row in list:
    print(row)