import sys 
sys.stdin = open("./Input_Data/D2/1928.txt")


B64_Idx='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
B64_Dic = {val: idx for idx, val in enumerate(B64_Idx)}

def B64_decode(s):
    bit=''; text=''
    for i in s:
        bit += bin(B64_Dic[i])[2:].zfill(6)
    for j in range(0,len(bit),8):
        text+=chr(int(bit[j:j+8], 2))
    return text

for T in range(int(input())):
    print('#{} {}'.format(T+1, B64_decode(input())))