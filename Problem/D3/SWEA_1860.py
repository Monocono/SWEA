import sys
sys.stdin = open("./Input_Data/D3/1860.txt","r")

for T in range(int(input())):
    n,m,k=map(int,input().split())
    person = list(map(int,input().split()))
    