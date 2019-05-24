##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
##
import itertools
from operator import itemgetter

csv = open('data.csv','r').readlines()
csv = [line[:-1] for line in csv]
csv = [line.split('\t') for line in csv]

allkeys = []
for keyset in [line[4].split(',') for line in csv]:
    allkeys += keyset
allkeys = [key.split(':') for key in allkeys]

for key, group in itertools.groupby(sorted(allkeys), itemgetter(0)):
    values = [int(line[1]) for line in group]
    print(key+','+str(min(values))+','+str(max(values)))