# UVA10420 -  List of Conquests  - Accepted
# goo.gl/Xe6I4R
# @author: Marcelo Adriano Amancio
# 'If the lessons of history teach us anything it is that nobody learns the lessons that history teaches us.' -- Anon
from sys import stdin

if __name__ == '__main__':
	n = int(stdin.readline())
	m = {}
	for cc in range(0,n):
		nat = stdin.readline().split()[0]
		m[nat] = (m[nat] + 1) if (nat in m) else 1 
	for key,value in sorted(m.items()):
		print('{} {}'.format(key,value))	
