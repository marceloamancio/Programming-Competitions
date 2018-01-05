# UVA369 - Combinations - Accepted
# goo.gl/ZhzrIh
# @author: Marcelo Adriano Amancio
# 'We are what we repeatedly do; excellence, then, is not an act but a habit.' -- Aristotle


from sys import stdin
from math import factorial

if __name__ == '__main__':
	n,m = map(int,stdin.readline().split())
	while (m or n):
		ans = factorial(n)//(factorial(n-m)*factorial(m))	
		print("{} things taken {} at a time is {} exactly.".format(n,m,ans))	
		n,m = map(int,stdin.readline().split())
		
