# UVA12503 - Robot Instructions - Accepted
# goo.gl/YViX00
# @author: Marcelo Adriano Amancio
# 'In the twenty-first century, the robot will take the place which slave labor occupied in ancient civilization. ' -- Nikola Tesla
from sys import stdin

if __name__ == '__main__':
    tc = int(stdin.readline())
    for _ in range(tc):
        n = int(stdin.readline())
        inst = []
        pos = 0
        for _ in range(n):
            li_s = stdin.readline()[:-1].split()
            li = -1 #LEFT
            if li_s[0] == 'RIGHT': li = +1
            elif li_s[0]=='SAME': li = inst[int(li_s[-1])-1]
            inst.append(li)
            pos += li
        print(pos)
