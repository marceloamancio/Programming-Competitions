# UVA12577 - Hajj-e-Akbar - Accepted
# goo.gl/dTcLVQ
# @author: Marcelo Adriano Amancio
# 'Imagination was given to man to compensate him for what he is not, and a sense of humor was provided to console him for what he is.' -- Oscar Wilde

from sys import stdin

if __name__ == '__main__':
	c = 1
	line = stdin.readline()
	while line != '*\n':
		r = 'Hajj-e-Akbar' if line == 'Hajj\n' else 'Hajj-e-Asghar'
		print('Case {}: {}'.format(c,r))
		c += 1
		line = stdin.readline()

			
