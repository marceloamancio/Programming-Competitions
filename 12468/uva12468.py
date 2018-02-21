# UVA12468 - Zapping  - Accepted
# goo.gl/8PhKV9
# @author: Marcelo Adriano Amancio
# 'If it weren't for electricity, we'd all be watching television by candlelight.' -- George Gobel



from sys import stdin

if __name__ == '__main__':
    while True:
        a,b = [int(x) for x in stdin.readline().split()]
        if a<0: break

        d = abs(a-b)
        dm = min(d,100-d)
        print(dm)
