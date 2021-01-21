import sys
sys.stdin=open("./input/2063.txt","r")

N=int(input())
list=list(map(int,input().split(" ")))
list.sort()
print(list[int((N-1)/2)])