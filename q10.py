##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
import csv

data = list(csv.reader(open('data.csv','r'), delimiter='\t'))

registers = [pair.split(':')[0] for row in data for pair in row[4].split(',')]
uniqueRegisters = set(registers)

for register in sorted(uniqueRegisters):
    print(register+','+str(registers.count(register)))