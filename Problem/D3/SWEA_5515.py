import sys
sys.stdin = open("./Input_Data/D3/5515.txt","r")

day =[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
num = [4,5,6,0,1,2,3]
for T in range(int(input())):
    m,d = map(int,input().split())
    print("#{} {}".format(T+1, num[sum(day[:m-1],d-1)%7]))