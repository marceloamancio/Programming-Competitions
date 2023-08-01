# UVA10812 - Beat the Spread! - Accepted
# goo.gl/Bj6JEx
# @author: Marcelo Adriano Amancio
# 'If you're trying to create a company, it's like baking a cake. You have to have all the ingredients in the right proportion.' -- Elon Musk 


from sys import stdin
from math import sqrt

if __name__ == '__main__':
	n = int(stdin.readline())
	for _ in range(n):
		p,m = map(int, stdin.readline().split())
		a = (p+m)//2
		b = (p-m)//2
		if a+b == p and a>=0 and b>=0:
			print (a,b)
		else:
			print('impossible')

		
		
	
