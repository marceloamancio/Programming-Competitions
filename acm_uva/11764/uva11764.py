# UVA11764  - Jumping Mario - Accepted
# goo.gl/UZ65wx
# @author: Marcelo Adriano Amancio
# 'The only exercise I excel at is jumping to conclusions. ' -- James Nathan Miller
from sys import stdin

if __name__ == '__main__':
    tc = int(stdin.readline())
    for i_tc in range(tc):

        stdin.readline()#discard line
        ll = [int(x) for x in stdin.readline().split()]
        cu, cd = 0,0
        for i in range(1,len(ll)):
            if ll[i-1] < ll[i]: cu += 1
            elif ll[i-1] > ll[i]: cd += 1
        print('Case %d: %d %d'%(i_tc+1,cu,cd))
