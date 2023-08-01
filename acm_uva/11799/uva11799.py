# UVA11799 -	Horror Dash  - Accepted
# goo.gl/sVh6Vh
# @author: Marcelo Adriano Amancio
# 'Where there is no imagination there is no horror.' -- Arthur Conan Doyle

from sys import stdin

if __name__ == "__main__":
    tc = int(stdin.readline())
    for i in range(tc):
        m = max([int(x) for x in stdin.readline().split()])
        print('Case %d: %d'%(i+1,m))
