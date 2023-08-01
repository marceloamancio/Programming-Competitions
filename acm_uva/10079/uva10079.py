
# UVA10079 -  Pizza Cutting - Accepted
# goo.gl/t0cU7H
# @author: Marcelo Adriano Amancio
# 'If there are no stupid questions, then what kind of questions do stupid people ask? Do they get smart just in time to ask questions?' -- Anon


from sys import stdin

if __name__ == '__main__':
	n = int(stdin.readline())
	while n>=0:
		ans = 1 + n*n - ((n-1)*n)//2
		print (ans)
		n = int(stdin.readline())
