import sys
sys.stdin = open("./Input_Data/D3/8673.txt","r")

for T in range(int(input())):
    k = int(input())
    l = list(map(int,input().strip().split()))
    temp = list()
    res = 0
    for i in range(k):
        for j in range(0,2**k,2):
            res += abs(l[j]-l[j+1])
            temp.append(l[j] if l[j]>l[j+1] else l[j+1])
        l, temp = temp ,l
        temp.clear()
        k -= 1
    print("#{} {}".format(T+1, res))

#solved