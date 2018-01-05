# UVA10300 - Ecological Premium - Accepted
# goo.gl/XxWLtL
# @author: Marcelo Adriano Amancio
# 'It's not what you look at that matters, it's what you see.' -- Henry David Thoreau


from sys import stdin

if __name__ == '__main__':
	n = int(stdin.readline())
	for _ in range(n):
		f = int(stdin.readline())
		cc=0
		for _ in range(f):
			a,_,b = map(int, stdin.readline().split())
			cc+= a*b
		print(cc)
		
