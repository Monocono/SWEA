import sys
sys.stdin = open("./Input_Data/D2/1859.txt", "r")

for T in range(int(input())):
    d=int(input())
    v=list(map(int,input().split(' ')))[::-1]
    m=v[0]
    res=0
    for i in v:
        if m>i:
            res+=m-i
        else:
            m=i
    print('#{} {}'.format(T+1,res))