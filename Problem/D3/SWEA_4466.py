import sys
from typing import Literal
sys.stdin = open("./Input_Data/D3/4466.txt","r")

for T in range(int(input())):
    n,k = map(int,input().strip().split())
    l = list(map(int,input().strip().split()))
    l.sort()
    l.reverse()
    print("#{} {}".format(T+1, sum(l[0:k])))