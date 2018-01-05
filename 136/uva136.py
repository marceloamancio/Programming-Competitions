# UVA136 - Ugly Numbers - Accepted
# goo.gl/4fqhyY
# @author: Marcelo Adriano Amancio
# 'A day without laughter is a day wasted.' -- Charlie Chaplin 

from heapq import heappush, heappop

if __name__ == '__main__':	
	h = []
	heappush(h, (1,2))
	cc = 0
	while cc<1500:
		num, father = heappop(h)
		for e in [2,3,5]:
			if e>=father:
				heappush(h, (num*e,e))
		cc+=1
	print("The 1500'th ugly number is {}.".format(num))
