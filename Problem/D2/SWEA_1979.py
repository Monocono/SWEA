import sys
sys.stdin = open("./Input_Data/D2/1979.txt","r")

for T in range(int(input())):
    n , k= map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    nums=[0]*(n+1)

    for i in range(n):
        cnt = 0; flag = False
        for j in range(1,n):
            if (not matrix[i][j] and matrix[i][j-1]) or (matrix[i][j] and not matrix[i][j-1]):
                if cnt>1 and not flag:
                    cnt +=1; nums[cnt] +=1; flag = True
                else:
                    cnt = 1
            elif matrix[i][j] and matrix[i][j-1]:
                cnt += 1
        if cnt and (not flag):
            nums[cnt] +=1

    for j in range(n):
        cnt = 0
        for i in range(1,n):
            if (not matrix[i][j] and matrix[i-1][j]) or (matrix[i][j] and not matrix[i-1][j]):
                if cnt:
                    cnt+=1
                else:
                    cnt = 1
            elif matrix[i][j] and matrix[i-1][j]:
                cnt += 1
        if cnt:
            nums[cnt] += 1
            
    print("#{} {}".format(T+1, nums[k]))
