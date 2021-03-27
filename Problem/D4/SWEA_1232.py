import sys
sys.stdin = open("./Input_Data/D4/1232.txt",'r')

def postorder(node):
    if node>=n:
        return
    if tree[node][2]:
        postorder(tree[node][2])
    if tree[node][3]:
        postorder(tree[node][3])
    if tree[node][1] =='+':
        tree[node][1] = tree[tree[node][2]][1] + tree[tree[node][3]][1]
    elif tree[node][1] =='-':
        tree[node][1] = tree[tree[node][2]][1] - tree[tree[node][3]][1]
    elif tree[node][1] =='*':
        tree[node][1] = tree[tree[node][2]][1] * tree[tree[node][3]][1]    
    elif tree[node][1] =='/':
        tree[node][1] = tree[tree[node][2]][1] // tree[tree[node][3]][1]

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
        if temp[1].isdigit():
            tree[node][1] = int(temp[1])
        else:
            tree[node][1]=temp[1]

    postorder(1)
    print("#{} {}".format(T+1, tree[1][1]))