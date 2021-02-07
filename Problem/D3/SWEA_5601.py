import sys
sys.stdin = open("./Input_Data/D3/5601.txt","r")

for T in range(int(input())):
    n = int(input())
    print("#{}".format(T+1),end=" ")
    for _ in range(n):
        print("{}/{}".format(1,n),end=" ")
    print()