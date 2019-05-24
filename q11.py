##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##
import csv

data = list(csv.reader(open('data.csv','r'), delimiter='\t'))

registers = [[row[0], str(len(row[3].split(','))), str(len(row[4].split(',')))] for row in data]
print('\n'.join([','.join(row) for row in registers]))