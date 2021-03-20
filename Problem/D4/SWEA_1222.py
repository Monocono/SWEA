import sys
sys.stdin = open('./Input_Data/D4/1222.txt','r')

def cal (t1, t2,op):
    t1 =int(t1)
    t2= int(t2)
    if op == '+': return t1+t2
    
for T in range(10):
    input()
    s = list(input())
    oper=[]
    num=[]
    for c in s:
        if '0' <= c <='9':
            num.append(c)
        else:
            oper.append(c)
    for op in oper:
        t2 = num.pop()
        t1 = num.pop()
        num.append(cal(t1,t2,op))
    print('#{} {}'.format(T+1, num[0]))