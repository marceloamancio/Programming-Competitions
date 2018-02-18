# UVA11559- Event Planning - Accepted
# goo.gl/oNif6E
# @author: Marcelo Adriano Amancio
# 'The great advantage of a hotel is that it is a refuge from home life.' -- George Bernard Shaw
from sys import stdin

def find_min_price(hotel, h, w, n):
    hotel = sorted(hotel,key=lambda a:a[0]) #sort by min price

    for i_h in range(h):
        for i_w in range(w):
            if hotel[i_h][1][i_w] >= n:
                return hotel[i_h][0] #return min_price

    return None

if __name__ == '__main__':
    line = stdin.readline()
    while len(line):
        n,b,h,w = [int(x) for x in line.split()]

        hotel = []
        for i in range(h):
            price = int(stdin.readline()[:-1])
            av_weeks = [int(x) for x in stdin.readline().split()]
            hotel.append((price,av_weeks))

        mp = find_min_price(hotel, h, w, n)


        if mp and (mp*n) <= b:
            print(mp*n)
        else:
            print('stay home')

        line = stdin.readline()
