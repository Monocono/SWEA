import sys
sys.stdin = open("./Input_Data/D3/5549.txt","r")

for T in range(int(input())):
    s=str(input())
    print("#{} {}".format(T+1, "Odd" if int(s[len(s)-1]) % 2 !=0 else "Even"))
    #solve