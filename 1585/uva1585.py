# UVA1585 - Score - Accepted
# goo.gl/Yq3ndr
# @author: Marcelo Adriano Amancio
# 'Getting old has its advantages. I can no longer read the bathroom scale.' -- Brad Schreiber

from sys import stdin

if __name__ == '__main__':
	n = int(stdin.readline())
	for _ in range(0,n):
		line = stdin.readline()

		c, lc = 0, 0
		for ch in line:
			if ch == 'O':
				lc +=1
				c += lc
			else:
				lc = 0

		print(c)





