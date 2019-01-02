import timeit
from ujson import loads
from time import time

import resource
def using(point=""):
      usage=resource.getrusage(resource.RUSAGE_SELF)
      return '''%s: usertime=%s systime=%s mem=%s mb
             '''%(point,usage[0],usage[1],
                  (usage[2]*resource.getpagesize())/1000000.0 )

def loads_json():
     f = open("FL.json","r")
     f = f.read()
     f = loads(f)
     f = f[0]
     print (len(f))
     print (f['333743'])
     #print (using())

def loads_csv():
    f = open("FL.csv","r")
    f = f.readlines()[1:]
    print (len(f))
    for i in f:
        if '333743' in i:
            print (i)
            break
    #print (using())


if __name__ == '__main__':
     print ("Json dump: ")
     #t = timeit.Timer(stmt="chec.loads_json()", setup="import chec")
     #print (t.timeit(1),'\n')
     ot = time()
     loads_json()
     print("time -",time()-ot)

     print ("csv dump: ")
     #t = timeit.Timer(stmt="chec.loads_csv()", setup="import chec")
     #print (t.timeit(1),"\n")
     ot = time()
     loads_csv()
     print("time -",time()-ot)
