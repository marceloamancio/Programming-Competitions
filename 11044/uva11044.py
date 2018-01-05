# UVA11044 - Searching for Nessy - Accepted
# goo.gl/A1Otmt
# @author: Marcelo Adriano Amancio
# 'Better to write for yourself and have no public, than to write for the public and have no self.' -- Cyril Connolly
from sys import stdin

if __name__ == '__main__':
	n = int(stdin.readline())
	for _ in range(n):
		m,n = map(int, stdin.readline().split())
		print((m//3)*(n//3))
