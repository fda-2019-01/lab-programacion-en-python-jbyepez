##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##
csv = open('data.csv','r').readlines()
csv = [line[:-1] for line in csv]
csv = [line.split('\t') for line in csv]
letters = [line[0] for line in csv]
for t in sorted([(l, letters.count(l)) for l in set(letters)]):
    print(t[0]+','+str(t[1]))