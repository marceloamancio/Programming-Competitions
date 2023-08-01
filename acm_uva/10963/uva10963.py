# UVA10963 - The Swallowing Ground - Accepted
# goo.gl/wpkOdM
# @author: Marcelo Adriano Amancio
# 'Only I can change my life. No one can do it for me.' -- Carol Burnett


from sys import stdin

if __name__ == '__main__':
	n = int(stdin.readline())
	for ii in range(n):
		stdin.readline()
		cols = int(stdin.readline())
		diff = None
		res = True
		for _ in range(cols):
			a,b = map(int,stdin.readline().split())
			if diff == None:
				diff = a-b
			else:
				if a-b != diff:
					res = False
		if ii!=0:
			print()
		print('yes' if res else 'no')
				
