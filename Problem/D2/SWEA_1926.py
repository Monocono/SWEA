import sys
sys.stdin = open("./Input_Data/D2/1926.txt","r")

for i in range(1,int(input())+1):
    n= sum(1 for x in str(i) if x in ['3','6','9'])
    if n==0:
        print(i, end=' ')
    else:
        print('-'*n, end=' ')