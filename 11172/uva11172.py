# UVA11172 - Relational Operator - Accepted
# goo.gl/0161s7
# @author: Marcelo Adriano Amancio
# 'You can do anything, but not everything..' -- David Allen


from sys import stdin

if __name__ == '__main__': 
	n = int(stdin.readline())
	for ii in range(0,n):
		a,b = map(int, stdin.readline().split())
		ch = '='
		ch = '<' if a<b else ch
		ch = '>' if a>b else ch
		print (ch)
		
