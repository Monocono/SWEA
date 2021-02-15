import sys
sys.stdin = open("./Input_Data/D3/8500.txt","r")

for T in range(int(input())):
    n = int(input())
    an = list(map(int,input().strip().split()))
    print("#{} {}".format(T+1, sum(an)+max(an)+n))
#solve