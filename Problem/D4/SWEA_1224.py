import sys
sys.stdin = open("./Input_Data/D4/1224.txt",'r')

priority ={'*':1,'+':2,'(':3,')':3}

def cal(t1,t2,op):
    t1 = int(t1)
    t2 = int(t2)
    if op == '+': return t1+t2
    elif op=='*': return t1*t2

for T in range(10):
    input()
    s=list(input())
    num = []
    oper=[]
    for c in s:
        if '0' <= c <= '9':
            num.append(c)
        elif not len(oper) or c =='(':
            oper.append(c)
        elif priority[c] < priority[oper[-1]] and c !=')':
            oper.append(c)
        else:
            while len(oper) and priority[c] >= priority[oper[-1]]:
                if oper[-1] == '(':
                    oper.pop()
                    break
                num.append(oper.pop())
            if c != ')':
                oper.append(c)

    while len(oper):
        num.append(oper.pop())

    for i in num:
        if '0'<= i <='9':
            oper.append(i)
        else:
            t2=oper.pop()
            t1=oper.pop()
            oper.append(cal(t1,t2,i))
    print("#{} {}".format(T+1,oper[0]))