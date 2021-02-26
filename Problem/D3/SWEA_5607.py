import sys
sys.stdin = open("./Input_Data/D3/5607.txt","r")

def factorial(n):
    f = 1
    for i in range(1,n+1):
        f*=i
    return f
for T in range(int(input())):
    n, r = map(int,input().split())
    print("#{} {:.0f}".format(T+1, (factorial(n)/(factorial(r)*factorial(n-r))%1234567891)))