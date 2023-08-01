# UVA483 - Word Scramble - Accepted
# goo.gl/bbhd1h
# @author: Marcelo Adriano Amancio
# 'Life shrinks or expands in proportion to one’s courage.' -- Anais Nin 


from sys import stdin

if __name__ == '__main__':
	line = stdin.readline()
	while line:
		line = line[:-1].split()
		first = True
		for w in line:
			ans = w[::-1]
			ans = ('' if first else ' ')  + ans
			first = False
			print(ans,end='')
			

		print('')
		line = stdin.readline()
	
