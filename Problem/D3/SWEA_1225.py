import sys
sys.stdin = open("./Input_Data/D3/1225.txt","r")

for _ in range(10):
    T = int(input())
    l = list(map(int,input().split()))
    k = 1
    while l[len(l)-1] !=0:
        if l[len(l)-1]<0:
            break
        l.append(0 if l[0]-k<0 else l[0]-k)
        l=l[1:]
        k+=1
        if(k>5): k=1
    print("#{}".format(T),end=" ")
    for _ in l:
        print(_,end=" ")
    print()