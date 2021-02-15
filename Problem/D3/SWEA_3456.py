import sys
sys.stdin = open("./Input_Data/D3/3456.txt","r")

for T in range(int(input())):
    a,b,c = map(int,input().strip().split())
    if a==b: res = c
    elif a==c: res = b
    else: res = a
    print("#{} {}".format(T+1,res))