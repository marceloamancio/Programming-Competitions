# UVA100 - The 3n + 1 Problem - Solved
# goo.gl/9FdJdO
# @author: Marcelo Adriano Amancio
# 'Imagination is more important than knowledge.' -- Albert Einstein

from sys import stdin

L = 10000000
hr = [None]*L
hr[1]=1
hr[0]=0

def f(i):
	if i<L:
		if hr[i] != None:
			return hr[i]
		
	ans = 1 + ( f(3*i+1) if i%2 else f(i//2) )
	if i<L:
		hr[i] = ans

	return ans 

def cl(a,b):
	maxn=0
	for x in range(a,b+1):
		maxn = max(f(x),maxn)
	return maxn

def main():
	for line in stdin:
		a,b = [int(s) for s in line.split()]
		print (a,b,cl(min(a,b),max(a,b)))

main()

