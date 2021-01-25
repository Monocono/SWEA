import sys
sys.stdin = open("./Input_Data/D1/2019.txt","r")

for i in range(int(input())+1):
    print(2**i, end=" ")