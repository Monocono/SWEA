import sys
sys.stdin = open("./Input_Data/D4/1233.txt",'r')

def inorder(node):
    if node:
        inorder(tree[node][2])
        tree_list.append(tree[node][1])
        inorder(tree[node][3])

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

    tree_list = []
    inorder(1)
    res = 1

    for i in range(len(tree_list)):
        if i%2 == 0:
            if ord(tree_list[i]) <48 or ord(tree_list[i]) >=58:
                res=0
                break
        else:
            if tree_list[i] not in ['+','-','*','/']:
                res = 0
                break
    print("#{} {}".format(T+1, res))