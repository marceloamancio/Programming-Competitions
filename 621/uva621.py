# UVA621 - Secret Research - Accepted
# goo.gl/o1COMR
# @author: Marcelo Adriano Amancio
# 'There is only one happiness in this life, to love and be loved.' -- George Sand


from sys import stdin
import re

if __name__ == '__main__':
	n = int(stdin.readline())
	for _ in range(n):
		e = stdin.readline()[:-1]
		if e in ('1','4','78'):
			print('+')
		elif re.match('^.*35$',e):
			print('-')
		elif re.match('^9.*4$',e):
			print('*')
		elif re.match('^190.*',e):
			print('?')

