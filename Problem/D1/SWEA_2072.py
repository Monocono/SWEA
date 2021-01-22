import sys
sys.stdin = open("./Input_Data/D1/2072.txt", "r")

for T in range(int(input())):
    list=map(int,input().split(' '))
    odd_list=[num for num in list if num % 2 == 1]
    print("#{} {}".format(T+1, sum(odd_list)))