import datetime
import csv
import matplotlib.pyplot as graph

e1 = []
e2 = []
w = []

with open('data.csv','r') as file:
    reader = csv.reader(file,delimiter=',')
    
    for row in reader:
        w.append(row[0])
        e1.append(row[1])
        e2.append(row[2])

    file.close()

n = w.__len__()

sume2e2 = 0
sumw = 0
sume2w = 0
sume2 = 0
sume2e1w = 0
sume1w = 0

for i in range(1,n):
    sumw = sumw + w[i]
    sume2 = sume2 + e2[i]
    sume2e2 = sume2e2 + (e2[i])**2
    sume2w = sume2w + e2[i]*w[i]
    sume2e1w = sume2e1w + e1[i]*e2[i]*w[i]
    sume1w = sume1w + e1[i]*w[i]

t = (sume2e2*sumw - sume2w*sume2)/(sume2e1w*sumw - sume2w*sume1w)

einf = (sume2e2*sume1w - sume2e1w*sume2)/(sume2e2*sumw - sume2w*sume2)

print("t = ",t)
print("einf = " ,einf)

rel_t = []

for i in range(0,n):
    t.append(e2[i]/((e1[i]-einf)*w[i]))

with open(f'data({datetime.datetime.now()}).csv','w') as file:
    writer = csv.writer(file,delimiter='/t')
    writer.writerows(zip(w,rel_t))
    file.close()

graph.plot(w,rel_t)
graph.xlabel("frequenecy")
graph.ylabel("relaxation time")
graph.title("relaxation time period variation with freq")
graph.show()

t = rel_t[0]

for i in range(1,n):
    t = t + rel_t[i]

print('t avg = ' , t/float(n))



