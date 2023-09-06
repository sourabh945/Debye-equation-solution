e1 = []
e2 = []
w = []

with open('data.dat','r') as file:
    
    for lines in file:
        w.append(lines.split()[0])
        e1.append(lines.split()[1])
        e2.append(lines.split()[2])

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


