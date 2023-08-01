# UVA10696 - f91 - Accepted
# goo.gl/hWu15p
# @author: Marcelo Adriano Amancio
# 'Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away.' -- Antoine de Saint-Exupéry

from sys import stdin

if __name__ == '__main__':
	while True:
		n = int(stdin.readline())
		if n==0:
			break
		ans = 91 if n<101 else n-10
		print("f91(%d) = %d"%(n,ans))
	
