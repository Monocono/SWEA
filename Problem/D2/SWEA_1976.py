import sys
sys.stdin = open("./Input_Data/D2/1976.txt","r")

for T in range(int(input())):
    h1,m1,h2,m2=map(int,input().split())
    h=h1+h2
    m=m1+m2
    if m >59:
        h+=1; m-=60
    if h>12: h-=12
    print("#{} {} {}".format(T+1,h,m))