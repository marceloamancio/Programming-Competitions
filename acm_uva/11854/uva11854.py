# UVA11854 - Egypt - Accepted
# goo.gl/hAni2T
# @author: Marcelo Adriano Amancio
# 'I always wanted to be somebody, but now I realize I should have been more specific.' -- Lily Tomlin


from sys import stdin

if __name__ == '__main__':
	a,b,c = map(int,stdin.readline().split())
	while a+b+c:
		v = sorted([a*a,b*b,c*c])
		if (v.count(0)==0) and (v[0]+v[1]==v[2]):
			print ('right')
		else:
			print ('wrong')

		a,b,c = map(int,stdin.readline().split())
		
