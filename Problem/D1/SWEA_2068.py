import sys
sys.stdin=open("./Input_Data/D1/2068.txt","r")

for T in range(int(input())):
    a = list(map(int, input().split()))
    print("#{} {}".format(T+1, max(a)))