import sys
sys.stdin = open("./Input_Data/D2/1284.txt","r")

for T in range(int(input())):
    p,q,r,s,w=map(int,input().split())
    A=w*p
    B=q if w<=r else q+s*(w-r)
    print("#{} {}".format(T+1,min(A,B)))