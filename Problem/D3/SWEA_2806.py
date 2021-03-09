import sys
sys.stdin = open("./Input_Data/D3/2806.txt",'r')

def nQueen(llist , n):
    global cnt
    if len(llist) == n:
        cnt += 1
        return
    candidate = list(range(n))
    for i in range(len(llist)):
        if llist[i] in candidate:
            candidate.remove(llist[i])
        dist = len(llist) - i
        if llist[i] - dist in candidate:
            candidate.remove(llist[i]-dist)
        if llist[i] + dist in candidate:
            candidate.remove(llist[i]+dist)
    if candidate:
        for i in candidate:
            nQueen(llist+[i],n)
    return

for T in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(n):
        nQueen([i],n)
    print("#{} {}".format(T+1, cnt))