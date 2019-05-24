##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##
import csv
from itertools import groupby
from operator import itemgetter

data = list(csv.reader(open('data.csv','r'), delimiter='\t'))

letters = [[letter, int(row[1])] for row in data for letter in row[3].split(',')]

lettersum = []
for key, group in groupby(sorted(letters),itemgetter(0)):
    lettersum += [[key, str(sum([row[1] for row in group]))]]
    
print('\n'.join([','.join(row) for row in lettersum]))