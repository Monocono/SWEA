import sys
sys.stdin = open("./Input_Data/D2/1204.txt","r")

for T in range(int(input())):
    t_n=int(input())
    s= list(map(int,input().split()))
    res= 0
    d = {}
    for i in s:
        if i in d:
            d[i] +=1
        else:
            d[i] =1
    
    m = 0
    for key, value in d.items():
        if m<value:
            m=value; res=key
        elif m == value:
            if res < key:
                res= key
    print("#{} {}".format(t_n,res))
