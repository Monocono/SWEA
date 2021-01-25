import sys
sys.stdin = open("./Input_Data/D1/2043.txt","r")

a,b= map(int, input().split())
print("{}".format(a-b+1 if a>b else 1000+a-b))