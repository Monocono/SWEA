import sys
sys.stdin = open("./Input_Data/D3/10804.txt","r")

for T in range(int(input())):
    s=str(input())
    res = ""
    for c in s[::-1]:
        if c == 'q': res+='p'
        elif c == 'p': res+='q'
        elif c == 'b': res+='d'
        else: res+='b'
    print("#{} {}".format(T+1,res))