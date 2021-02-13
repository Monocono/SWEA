import sys
sys.stdin = open("./Input_Data/D3/1240.txt","r")

nums = ["0001101","0011001","0010011","0111101","0100011","0110001","0101111","0111011","0110111","0001011"]

for T in range(int(input())):
    n,m = map(int,input().split())
    row=""
    l = [list(map(str,input().strip())) for _ in range(n)]
    for i in range(n):
        temp = ''.join(l[i])
        if temp.count('1') > 1:
            row = temp
            break
    idx = row.rindex('1')
    row = row[idx-55:idx+1]
    code =""
    res = 0
    for i in range(8):
        if row[i*7:i*7+7] in nums:
            code+=str(nums.index(row[i*7:i*7+7]))
        else:
            break
    check = sum(int(code[i]) for i in range(0,7,2))*3 + sum(int(code[j]) for j in range(1,8,2))
    if check > 9 and check % 10 == 0:
        for i in range(8):
            res += int(code[i])
    print("#{} {}".format(T+1,res))