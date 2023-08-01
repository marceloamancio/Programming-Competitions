# UVA12646 - Zero or One - Accepted
# goo.gl/OguK9v
# @author: Marcelo Adriano Amancio
# 'When a person can no longer laugh at himself, it is time for others to laugh at him.' -- Thomas Szasz

from sys import stdin

if __name__ == '__main__':
	line = stdin.readline()
	while line:
		a,b,c = map(int, line.split())
		if a*b*c or (a+b+c == 0):
			print('*')
		elif b==c:
			print('A')
		elif a==c:
			print('B')
		else:
			print('C')

		line = stdin.readline()
