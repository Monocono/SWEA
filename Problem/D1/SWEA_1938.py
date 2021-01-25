import sys
sys.stdin = open("./Input_Data/D1/1938.txt","r")

a,b=map(int, input().split(" "))
for e in [a+b, a-b,a*b,a//b]:
    print(e)