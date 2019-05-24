##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##
import csv

data = list(csv.reader(open('data.csv','r'), delimiter='\t'))

row5sum = [[row[0], str(sum([int(val.split(':')[1]) for val in row[4].split(',')]))] for row in data]
print('\n'.join([','.join(row) for row in row5sum]))