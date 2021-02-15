from io import SEEK_END
import sys
sys.stdin=open("./Input_Data/D3/7102.txt","r")

for T in range(int(input())):
    n, m = map(int,input().split())
    l = [0]*(n+m)
    for i in range(1,n):
        for j in range(1,m):
                l[i+j]+=1
    print('#{}'.format(T+1),end=' ')
    for i in range(n+m):
        if l[i] == max(l):
            print("{}".format(i+1),end=' ')
    print()