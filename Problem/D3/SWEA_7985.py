import sys
sys.stdin = open("./Input_Data/D3/7985.txt","r")

for T in range(int(input())):
    k = int(input())
    l = list(map(int,input().split()))

    for i in range(k):
        for j in range(pow(2,i)):
            