import sys
sys.stdin=open("./input/2071.txt","r")

for T in range(int(input())):
    list=map(int,input().split(" "))
    print("#{} {}".format(T+1, round(sum(list)/10)))