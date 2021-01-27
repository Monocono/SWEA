import sys
sys.stdin=open("./Input_Data/D2/1989.txt","r")

for T in range(int(input())):
    s=input().strip()
    print("#{} {}".format(T+1,int(s==s[::-1])))