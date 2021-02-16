import sys
sys.stdin = open("./Input_Data/D3/3142.txt","r")

for T in range(int(input())):
    n, m = map(int,input().strip().split())
    print("#{} {} {}".format(T+1, 2*m-n, m-(2*m-n)))