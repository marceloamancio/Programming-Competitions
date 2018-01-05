# UVA834 - Continued Fractions - Accepted
# goo.gl/F7SjO7
# @author: Marcelo Adriano Amancio
# 'To the man who only has a hammer, everything he encounters begins to look like a nail.' -- Abraham Maslow

from sys import stdin

def process(a,b):
	ch = ';'
	print("[{}".format(a//b),end='')

	a,b = b,a%b 
	while b:
		print('{}{}'.format(ch,format(a//b)),end='')
		a,b = b,a%b
		ch = ','
	print(']')
			

if __name__ == '__main__':
	line = stdin.readline()
	while line:
		a,b = map(int,line.split())
		process(a,b)
		line = stdin.readline()
