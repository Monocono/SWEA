import sys
sys.stdin = open("./Input_Data/D3/1216.txt","r")

for T in range(10):
    n = 100
    k, res = 1,1
    tc = int(input())
    rl = [list(map(str,input())) for _ in range(n)]
    cl = list(map(list,zip(*rl)))
    flag = False
    for a in range(100):
        flag = False
        for b in range(100):
            for c in range(101-k):
                row = rl[b][c:c+k]
                col = cl[b][c:c+k]
                if row == row[::-1] or col == col[::-1]:
                    res = k
                    flag = True
                    break
            if flag:
                break
        k +=1
    print("#{} {}".format(tc, res))

# 시간이 너무 오래걸림


def is_palindrome1(a, n, m):
    for i in range(n):
        for j in range(n - m + 1):
            for k in range(m // 2):
                if a[i][j + k] != a[i][j + m - 1 - k]:
                    break
            else:
                return m
    return 0
 
 
def is_palindrome2(a, n, m):
    for i in range(n):
        for j in range(n - m + 1):
            # if list(a[i])[j:j+m] == list(reversed(list(a[i])[j:j+m])):
            if a[i][j:j+m] == (a[i][j:j+m])[::-1]:
                return m
    return 0
 
 
def is_palindrome3(a, n, m):
    for i in range(n):
        for j in range(n - m + 1):
            b = list(a[i])[j:j + m]
            if b == b[::-1]:
                return m
    return 0
 
 
def solution():
    n = 100
    m = int(input())
    a = [list(input()) for _ in range(n)]
 
    maxLength = 1
    m = maxLength + 1
    while m <= 100 and m <= maxLength + 2:
        if maxLength < is_palindrome1(a, n, m):
            maxLength = m
        m += 1
    m = maxLength + 1
    while m <= 100 and m <= maxLength + 2:
        if maxLength < is_palindrome1(list(zip(*a)), n, m):
            maxLength = m
        m += 1
 
    return maxLength
 
 
def main():
    T = 10
    for test_case in range(1, T + 1):
        print("#{} {}".format(test_case, solution()))
 
 
if __name__ == "__main__":
    main()