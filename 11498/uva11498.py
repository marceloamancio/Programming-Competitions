# UVA11498 - Division of Nlogonia - Accepted
# goo.gl/6eB0YT
# @author: Marcelo Adriano Amancio
# 'Never be afraid to laugh at yourself, after all, you could be missing out on the joke of the century.' -- Dame Edna Everage 
from sys import stdin

if __name__ == '__main__':
	n = int(stdin.readline())
	while n:
		x,y = map(int, stdin.readline().split())
		for _ in range(n):
			a,b = map(int, stdin.readline().split())
			if a==x or b==y:
				print('divisa')	
			elif a>x and b>y:
				print('NE')
			elif a>x and b<y:
				print('SE')
			elif b>y:
				print('NO')
			else:
				print('SO')

		n = int(stdin.readline())
