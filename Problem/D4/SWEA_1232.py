import sys
sys.stdin = open("./Input_Data/D4/1232.txt",'r')

def postorder(node):
    if node:
        return
for T in range(10):
    n = int(input())
    tree = [[0 for _ in range(4)] for _ in range(n+1)]

    for line in range(n):
        temp=list(input().split())
        node=int(temp[0])
        tree[node][0]=node
        if len(temp) >= 3 :
            tree[node][2]=int(temp[2]) 
        if len(temp) == 4 :
            tree[node][3]=int(temp[3])
        tree[node][1]=temp[1]

    postorder(1)
    print("#{} {}".format())