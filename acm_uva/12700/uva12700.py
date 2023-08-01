# UVA12700 - Banglawash - Accepted
# goo.gl/azPZq1
# @author: Marcelo Adriano Amancio
# 'Tomorrow is often the busiest day of the week.' -- Spanish Proverb


from sys import stdin
from collections import Counter

if __name__ == '__main__':
	n = int(stdin.readline())
	c = 1
	for _ in range(n):
		nt = int(stdin.readline())
		g = Counter(stdin.readline()[:-1])
		a,t,b,w = g['A'], g['T'], g['B'], g['W']
		
		if a == nt:
			print('Case {}: ABANDONED'.format(c))
		elif (a+w) == nt:
			print('Case {}: WHITEWASH'.format(c))
		elif (a+b) == nt:
			print('Case {}: BANGLAWASH'.format(c))
		elif b == w:
			print('Case {}: DRAW {} {}'.format(c,b,t))
		elif b > w:
			print('Case {}: BANGLADESH {} - {}'.format(c,b,w))
		elif w > b:
			print('Case {}: WWW {} - {}'.format(c,w,b))
		c+=1
			

		
