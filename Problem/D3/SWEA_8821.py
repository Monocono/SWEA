import sys
sys.stdin = open("./Input_Data/D3/8821.txt","r")

for T in range(int(input())):
    s=str(input())
    res = []
    for i in range(len(s)):
        if s[i] in res: res.pop(res.index(s[i]))
        else: res.append(s[i])
    print("#{} {}".format(T+1, len(res)))

#solve