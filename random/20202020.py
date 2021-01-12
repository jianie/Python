import random
tries=0
count=0
for i in range(int(1000000/5)):
    findflag = False
    tries+=1
    ballist = random.sample(range(1, 60), 5)
    ballist.append(random.randint(1,35))
    for j in range(0,5,1):
        for k in range(j,5,1):
            if abs(ballist[j]-ballist[k])==1:
                findflag=True
                break
        if findflag:
            count+=1
            break
percent=(count/(tries))
print("{0:.0%} of the time there were at least\ntwo consecutive numbers in the set\nof five numbers.".format(percent))