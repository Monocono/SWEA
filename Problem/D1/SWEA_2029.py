import sys
sys.stdin = open("./Input_Data/D1/2029.txt","r")

for T in range(int(input())):
    a,b=map(int, input().split(" "))
    print("#{} {} {}".format(T+1, a//b, a%b))