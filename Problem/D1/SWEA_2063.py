import sys
sys.stdin=open("./Input_Data/D1/2063.txt","r")

N=int(input())
a=list(map(int,input().split(" ")))
print(a)
a.sort()
print(a[int((N-1)/2)])