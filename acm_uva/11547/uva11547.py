# UVA11547 - Automatic Answer - Accepted
# goo.gl/EDyyCY
# @author: Marcelo Adriano Amancio
# 'The greatest obstacle to discovery is not ignorance; it is the illusion of knowledge.' -- Daniel J. Boorstin


from sys import stdin

if __name__ == '__main__':
	n = int(stdin.readline())
	for _ in range(n):
		e = int(stdin.readline())
		v =  abs(e*315 + 36962) %100
		v = v//10
		print(v)
