import sys
sys.stdin = open("./Input_Data/D2/1961.txt","r")

def rotate(a,n):
    temp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[j][n-1-i] = a[i][j]
    return temp

for T in range(int(input())):
    N = int(input())
    matrix =[list(map(int,input().split())) for _ in range(N)]

    a = rotate(matrix,N)
    b = rotate(a, N)
    c = rotate(b, N)

    print("#{}".format(T+1))
    for i in range(N):
        print(''.join(map(str,a[i])),''.join(map(str,b[i])),''.join(map(str,c[i])))