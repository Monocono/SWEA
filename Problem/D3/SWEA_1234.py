import sys
sys.stdin = open("./Input_Data/D3/1234.txt","r")

for T in range(10):
    n, s = map(str,input().split())
    res = ''
    for i in s:
        if len(res) >0 and res[-1] == i:
            res = res[:-1]
        else:
            res += i
    print("#{} {}".format(T+1, res))