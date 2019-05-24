##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##
csv = open('data.csv','r').readlines()
csv = [line[:-1] for line in csv]
csv = [line.split('\t') for line in csv]

LineMonths = [line[2].split('-')[1] for line in csv]
months = set(LineMonths)
for t in sorted(months):
    print(t+','+str(LineMonths.count(t)))