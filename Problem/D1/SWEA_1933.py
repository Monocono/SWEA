import sys
sys.stdin = open("./Input_Data/D1/1933.txt","r")

a= int(input())
for i in range(1,a+1):
    if a%i == 0:
        print(i, end=' ')
    
