from random import randint as ri
from random import uniform as ui
import sys

def get_csv(nums):
    res = ["key,val,randnu"]
    rand_da = ['app','bal','cat','mic','lio','pea','dog','ban','hor','mou']
    for i in range(nums):
        res.append("%s,%s,%s"%(ri(0,100000),rand_da[int(ui(0,len(rand_da)-1))],ri(77,78236487)))
    return "\n".join(res)

if __name__ == "__main__":
    print(sys.argv)
    try:
        filen = sys.argv[2]
    except:
        filen = "output.csv"

    try:
        rows = int(sys.argv[1])
    except:
        rows = 10
    with open(filen,"w") as f:
        f.write(get_csv(rows))
