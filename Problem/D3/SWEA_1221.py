import sys
sys.stdin = open("./Input_Data/D3/1221.txt","r")

''' solution #1 using list - runtime error
NumToStr = ["ZRO","ONE","TWO","THR","FOR","FIV","SIX",'SVN',"EGT","NIN"]

for T in range(int(input())):
    t, n = map(str,input().split())
    ori_s = list(map(str,input().strip().split()))
    sToNum =[]
    for s in ori_s:
        sToNum.append(NumToStr.index(s))
    sToNum.sort()
    print("{}".format(t))
    print(" ".join(NumToStr[n] for n in sToNum))
'''

# solution #2 using dict - pass
for T in range(int(input())):
    NumToStr = {'ZRO': 0,'ONE': 0,'TWO': 0,'THR': 0,'FOR': 0,'FIV': 0,'SIX': 0,'SVN': 0,'EGT': 0,'NIN': 0}
    t, n=map(str,input().split())
    ori_s = list(map(str,input().strip().split()))
    res = ''
    for s in ori_s: NumToStr[s] +=1
    for key,value in NumToStr.items():
        temp = ' '.join([key]*value)
        res += temp+' '
    print("{}".format(t))
    print(res[:len(res)-1])