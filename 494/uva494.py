# UVA494 - Kindergarten Counting Game - Accepted
# goo.gl/2uGkg5
# @author: Marcelo Adriano Amancio
# 'Could it think, the heart would stop beating..' -- Fernando Pessoa


from sys import stdin

def main():
	last_isalpha = False
	count = 0
	while True:
		c = stdin.read(1)

		if len(c) == 0:
			break
		elif c=='\n':
			print (count)
			last_isalpha = False
			count = 0
		elif c.isalpha() != last_isalpha:
			if c.isalpha():
				count += 1
			last_isalpha = c.isalpha()

main()
