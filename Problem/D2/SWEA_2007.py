import sys
sys.stdin= open("./Input_Data/D2/2007.txt","r")

for T in range(int(input())):
    s=input()
    for i in range(1,10):
        if s[:i]==s[i:2*i]:
            print("#{} {}".format(T+1, i))
            break

#추가조건 : 패턴의 길이가 가장 작은것 