import sys
sys.stdin = open("./Input_Data/D3/4751.txt","r")

for T in range(int(input())):
    word = input()
    a = '..#.'
    b = '.#.#'
    ab_last = '.'
    c1 = '#.'
    c2 = '.'
    c_last = '#'

    N = len(word)
    answer = ['']*5
    answer[0] += a*N + ab_last
    answer[1] += b*N + ab_last
    for w in word:
        answer[2] += c1 + w + c2
    answer[2] += c_last
    answer[3] += b*N + ab_last
    answer[4] += a*N + ab_last

    for rw in answer:
        print(rw) 