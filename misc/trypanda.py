import pandas
import time
st = time.time()
csv = pandas.read_csv("fif.csv")

hed = list(csv)

key = "randnu"

if key not in hed:
    exit()

rows = csv.shape[0]

dic = {}

for i in range(rows):
    temp={}
    for h in hed:
        if h != key:
            temp.update({h:csv[h][i]})
    dic.update({csv[key][i]:temp})

print(time.time()-st)
print(len(dic))
