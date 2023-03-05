numstr = input()
num = int(numstr)

number = []
numberstr = input().split()

count = 0

for p in range(num):
    number.append(int(numberstr[p]))
number.sort()

i = 0
dup = None

for i in range(num-1):
    if number[i]==dup:
        i += 1
        continue
    dup = number[i]

    j = i+1
    k = num-1
    prv1 = number[j]-1
    while j<k:
        if number[i]+number[j]+number[k]>0:
            k -= 1
        elif number[i]+number[j]+number[k]<0:
            j += 1
        elif number[i]+number[j]+number[k]==0:
            if prv1 != number[j]:
                count += 1
                prv1 = number[j]
            k -= 1
            j += 1
    i += 1

print(count)