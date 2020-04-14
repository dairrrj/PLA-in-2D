import numpy as np
import matplotlib.pyplot as plt
fid = open("D:\\train.txt")
lines = fid.readlines()
data_load = []
positive_point=[]
negative_point=[]
for line in lines:
    line = line.strip('\n')
    line_split = line.split('\t')
    data_load.append([float(line_split[0]),float(line_split[1]),line_split[2]])

wr0=1
wr1=1
wr2=1
wr=np.array([wr0,wr1,wr2])
ii=1
while True:
    ii=ii+1
    iscompleted= True
    wr0=wr[0]
    wr1=wr[1]
    wr2=wr[2]
    for j in range(len(data_load)):
        x1=data_load[j][0]
        x2=data_load[j][1]
        xnt=np.array([1,x1,x2])
        
        if data_load[j][2] == '+':
            sign_o=1
        else:
            sign_o=-1
        yn=wr1*x1+wr2*x2+wr0
        if yn > 0:
            sign_n=1
        elif yn < 0:
            sign_n=-1

        if sign_o == sign_n:
            continue
        else:
            iscompleted = False
            wr=wr-sign_n*xnt

    if iscompleted:
        print(ii)
        break

for k in range(len(data_load)):
    x1=data_load[k][0]
    x2=data_load[k][1]
    if data_load[k][2] == '+':
        positive_point.append([x1,x2])
    else:
        negative_point.append([x1,x2])
positive_point=np.array(positive_point)
negative_point=np.array(negative_point)

xx1 = np.arange(-150,150,0.2)
xx2 = -wr[1]/wr[2]*xx1-wr[0]/wr[2]
plt.plot(xx1,xx2)
plt.xlabel('x1')
plt.ylabel('x2')
plt.scatter(positive_point[:,0],positive_point[:,1],s=20,marker='o',c='',edgecolors= '#0000FF')
plt.scatter(negative_point[:,0],negative_point[:,1],s=20,marker='x',c='r')
plt.show()

