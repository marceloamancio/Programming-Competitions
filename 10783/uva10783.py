# UVA10783 - Odd Sum - Accepted
# goo.gl/IsBcJJ
# @author: Marcelo Adriano Amancio
# 'Learning is forgetting the details as much as it is remembering the important parts.' --  Pedro Domingos


from sys import stdin

if __name__ == '__main__':
	n = int(stdin.readline())
	cc=1
	for _ in range(n):
		a = int(stdin.readline())
		b = int(stdin.readline())
		r = ((b+1)//2)**2 - (a//2)**2
		print ('Case {}: {}'.format(cc, r))
		cc += 1



