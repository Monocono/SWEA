import sys
sys.stdin = open("./Input_Data/D3/1240.txt","r")

for T in range(int(input())):
    n,m = map(int,input().strip().split())
    l = [list(map(str,input().strip())) for _ in range(n)]
    