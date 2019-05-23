##
## Imprima la suma de la segunda columna.
##
text = open('data.csv','rt').readlines()
text = [line[:-1] for line in text]
csv = [line.split('\t') for line in text]
print(sum([int(line[1]) for line in csv]))