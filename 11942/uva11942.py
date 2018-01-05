# UVA11942 - Lumberjack Sequencing - Accepted
# goo.gl/OFleU2
# @author: Marcelo Adriano Amancio
# 'If I only had a little humility, I’d be perfect' -- Ted Turner


from sys import stdin

if __name__ == '__main__':
	n = int(stdin.readline())
	print('Lumberjacks:')
	for _ in range(n):
		l = [int(x) for x in stdin.readline().split()]
		if l[-1]<l[0]:
			l = l[::-1]
		std = True
		for i in range(1,len(l)):
			if l[i-1] > l[i]:
				
				std = False
				break
		if std:
			print('Ordered')
		else:	
			print('Unordered')
