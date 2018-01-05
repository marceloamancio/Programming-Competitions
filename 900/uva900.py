# UVA900 - Brick Wall Patterns - Accepted
# goo.gl/01ffgT
# @author: Marcelo Adriano Amancio
# 'I took a speed reading course and read ‘War and Peace’ in twenty minutes. It involves Russia.' -- Woody Allen 

from sys import stdin

if __name__ == '__main__':
	l = [1,1,2,3]
	for i in range(4,60):
		l.append(2*l[i-2]+l[i-3])
	n = int(stdin.readline())
	while n:
		print(l[n])
		n = int(stdin.readline())

