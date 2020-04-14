import random
import numpy as np
import sys

#def DataEmit(sys.argv[1],sys.argv[2],sys.argv[3]):
w=sys.argv[1]
w=w.strip('[')
w=w.strip(']')
w_split=w.split(',')
w0= int(w_split[0])
w1= int(w_split[1])
w2= int(w_split[2])
m= int(sys.argv[2])
n= int(sys.argv[3])

train=[]
i1=1
i2=1
ii=1
while ii < 200:
    if i1 <= m and i2 <= n:
        x1=random.uniform(-150,150)
        x2=random.uniform(-150,150)
        x1=round(x1,2)
        x2=round(x2,2)
        sign=w1*x1+w2*x2+w0
        if sign>=0:
            newdata=[x1,x2,'+']
            train.append(newdata)
            i1=i1+1
            ii=ii+1
            continue
        elif sign<0:
            newdata=[x1,x2,'-']
            train.append(newdata)
            i2=i2+1
            ii=ii+1
            continue
    elif i1 > m and i2 <= n:
        x1=random.uniform(-150,150)
        x2=random.uniform(-150,150)
        x1=round(x1,2)
        x2=round(x2,2)
        sign=w1*x1+w2*x2+w0
        if sign<0:
            newdata=[x1,x2,'-']
            train.append(newdata)
            i2=i2+1
            ii=ii+1
            continue
    elif i1 <= m and i2 > n:
        x1=random.uniform(-150,150)
        x2=random.uniform(-150,150)
        x1=round(x1,2)
        x2=round(x2,2)
        sign=w1*x1+w2*x2+w0
        if sign>0:
            newdata=[x1,x2,'+']
            train.append(newdata)
            i1=i1+1
            ii=ii+1
            continue
    elif i1 > m and i2 > n:
        break
        print (train)
savepath = "D:\\train.txt"
with open(savepath,'w') as f:
    for item in train:
        f.write("%s\t%s\t%s\n" % (item[0],item[1],item[2]))

