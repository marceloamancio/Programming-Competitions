# UVA12149 - Feynman - Accepted
# goo.gl/Y7pxsZ
# @author: Marcelo Adriano Amancio
# 'Hofstadter’s Law: It always takes longer than you expect, even when you take into account Hofstadter’s Law.' -- Douglas Hofstadter


from sys import stdin

if __name__ == '__main__':
	n = int(stdin.readline())
	while n:
		#print(sum([x**2 for x in range(1,n+1)]))
		print( (n*(n+1)*(2*n+1))//6) #we've got a formula for that
		n = int(stdin.readline())
