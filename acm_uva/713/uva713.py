# UVA713 -  Adding Reversed Numbers - Accepted
# goo.gl/ENPiFP
# @author: Marcelo Adriano Amancio
# 'No intelligent idea can gain general acceptance unless some stupidity is mixed in with it.' -- Fernando Pessoa

from sys import stdin

def invn(e):
	inv = 0
	while e>0:
		inv = inv*10 + e%10
		e = e//10
	return inv	

if __name__ == '__main__':
	n = int(stdin.readline())
	for i in range(0,n):
		a,b = map(int, stdin.readline().split())
		print(invn(invn(a)+invn(b)))
