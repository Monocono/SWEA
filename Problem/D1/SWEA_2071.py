import sys
sys.stdin=open("./Input_Data/D1/2071.txt","r")

for T in range(int(input())):
    list=map(int,input().split(" "))
    print("#{} {}".format(T+1, round(sum(list)/10)))