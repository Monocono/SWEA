import sys
sys.stdin = open("./Input_Data/D2/1970.txt","r")

currency=[50000,10000,5000,1000,500,100,50,10]
for T in range(int(input())):
    m = int(input())
    res=[]
    while m > 9:
        for i in range(len(currency)):
            if m < currency[i]:
                res.append(0)
            else:
                res.append(m//currency[i])
                m-=res[i]*currency[i]
    print("#{}".format(T+1))
    for _ in res:
        print(_ ,end=' ')
    print()