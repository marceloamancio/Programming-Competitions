# UVA11679 - Sub-prime - Accepted
# goo.gl/788UiP
# @author: Marcelo Adriano Amancio
# 'Rather go to bed with out dinner than to rise in debt.' -- Benjamin Franklin
from sys import stdin

if __name__ == '__main__':
    i = 0
    while True:
        i += 1
        b,n = [int(x) for x in stdin.readline().split()]
        if b+n == 0: break

        banks_cash = [int(x) for x in stdin.readline().split()]
        for _ in range(n):
            d,c,v = [int(x) for x in stdin.readline().split()]
            d,c = d-1, c-1
            banks_cash[d] -= v
            banks_cash[c] += v
        possible = True
        for e in banks_cash:
            if e<0:
                possible = False
                break
        print('S' if possible else 'N')
