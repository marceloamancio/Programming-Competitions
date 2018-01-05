# UVA12895 - Armstrong Number - Accepted
# goo.gl/T9W40Z
# @author: Marcelo Adriano Amancio
# 'Be yourself; everyone else is already taken.' -- Oscar Wilde


from sys import stdin

if __name__ == '__main__':
	n = int(stdin.readline())
	for _ in range(n):
		line = stdin.readline()[:-1]
		ll = len(line)
		c = 0
		for e in line:
			c += int(e)**ll

		if str(c) == line:
			print('Armstrong')
		else:
			print('Not Armstrong')
