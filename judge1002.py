pnumstr = input()
pnum = int(pnumstr)
studentnumstr = [None]*1000
studentnum = [None]*1000
studentnum2 = [None]*1000
a = []

for i in range(pnum):
    studentnumstr[i] = input()
    studentnum[i] = int(studentnumstr[i])

for p1 in range(pnum):
    for p2 in range(2,4):
        a.append(studentnumstr[p1][p2])

for p3 in range(0,pnum*2,2):
    print(a[p3], end='')
    print(a[p3+1])
    