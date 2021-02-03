import sys
sys.stdin = open("./Input_Data/D2/1966.txt", "r")

for T in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))
    s.sort()
    print("#{}".format(T+1),end=" ")
    for c in s:
        print(c, end=" ")
    print()