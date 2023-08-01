# UVA12372 - Packing for Holiday - Accepted
# goo.gl/IBB9Jz
# @author: Marcelo Adriano Amancio
# 'Honest criticism is hard to take, particularly from a relative, a friend, an acquaintance, or a stranger.' -- Franklin P. Jones 


from sys import stdin

if __name__ == '__main__':
	n = int(stdin.readline())
	cc = 1
	for _ in range(n):
		a,b,c = map(int,stdin.readline().split())
		res = 'good'
		if a>20 or b>20 or c>20:
			res = 'bad'
		print('Case {}: {}'.format(cc,res))

		cc += 1	
