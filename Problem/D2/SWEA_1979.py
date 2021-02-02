import sys
sys.stdin = open("./Input_Data/D2/1979.txt","r")

for T in range(int(input())):
    n , k= map(int,input().split())
    matrix = [[0]*(n+2) for _ in range(n+2)]
    for i in range (1, n+1):
        matrix[i] = [0]+list(map(int,input().split()))+[0]

    row=col=0
    for i in range(1,n+1):
        cnt = 0
        for j in range(n+1):
            if matrix[i][j] == 0:
                if matrix[i][j] != matrix[i][j+1]:
                    cnt+=1
            else:
                if matrix[i][j]==matrix[i][j+1]:
                    cnt+=1
                else:
                    if cnt == k:
                        row+=1
                    cnt=0

    for i in range(1,n+1):
        cnt = 0
        for j in range(n+1):
            if matrix[j][i] == 0:
                if matrix[j][i] != matrix[j+1][i]:
                    cnt+=1
            else:
                if matrix[j][i]== matrix[j+1][i]:
                    cnt+=1
                else:
                    if cnt == k:
                        col+=1
                    cnt = 0
            
    print("#{} {}".format(T+1, row+col))
