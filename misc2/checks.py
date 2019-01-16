from csvtojson import write_csv_json
from time import time
from json import loads
src = "output.csv"
des = "out.json"

st = time()
write_csv_json(src,des,pkey="key",header=True)
print("convert to csv -->",time()-st)

st = time()
l = None
with open(des,"r") as d:
    l = d.read()
    l = loads(l)
print("read from json -->",time()-st)


st
a = []
with open(src,"r") as d:
    for i in d:
        a.append(i.strip().split(","))

print("read from csv -->",time()-st)

ke = [62033,99180,80351,15222,37289478923,7467,98740,74002,828,88720,6328746,46512,44756,86797,81765]
ke = list(map(str,ke))
print (ke)
st = time()
for k in ke:
    if k in l[0]:
        print ("from dict",k)
    else:
        print ("from dict, %s not found"%(k))
print("dict access",time()-st)

st = time()
for k in ke:
    flag = True
    for i in a:
        if k == i[0]:
            flag = False
            break
    if flag:
        print("from csv, %s not found"%(k))
print("csv access",time()-st)
