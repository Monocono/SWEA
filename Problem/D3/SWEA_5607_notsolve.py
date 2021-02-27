import sys
sys.stdin = open("./Input_Data/D3/5607.txt","r")

def factorial(n):
    f = 1
    for i in range(1,n+1):
        f*=i
    return f
def binoCoef(n,k):
    if k>n: return 0
    if k == 0 or k == n: return 1
    return binoCoef(n-1,k-1,) + binoCoef(n-1,k)

for T in range(int(input())):
    n, r = map(int,input().split())
    print("#{} {:.0f}".format(T+1, binoCoef(n,r)%1234567891))