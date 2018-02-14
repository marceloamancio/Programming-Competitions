
# UVA573 - The Snail - Accepted
# goo.gl/qTkHJk
# @author: Marcelo Adriano Amancio
# 'In philosophy if you aren't moving at a snail's pace you aren't moving at all.' -- Iris Murdoch
from sys import stdin

if __name__ == '__main__':
    h,u,d,f = [int(x) for x in stdin.readline().split()]
    while h!=0:
        df = u * (f / 100)
        day, hs, result = 1,0,0
        while result == 0:
            #day
            hs += u
            if hs>h:
                result = 1
                break
            #night
            hs -= d
            if hs < 0:
                result = -1
                break
            #params for next day
            u = max(0, u-df)
            day += 1
        h,u,d,f = [int(x) for x in stdin.readline().split()]
        print('success' if result>0 else 'failure','on day',day)
