import sys
sys.stdin = open("./Input_Data/D3/10200.txt","r")

for T in range(int(input())):
    n, a,b = map(int,input().split())
    print("#{} {} {}".format(T+1, min(a,b) , max(a+b-n,0)))