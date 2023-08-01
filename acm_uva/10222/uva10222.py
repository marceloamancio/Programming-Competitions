# UVA10222 -  Decode the Mad man  - Accepted
# goo.gl/wIf0bV
# @author: Marcelo Adriano Amancio
# 'Whatever you are, be a good one.' -- Abraham Lincoln
from sys import stdin

if __name__ == '__main__':
	
	k = "`1234567890-=qwertyuiop[]\\asdfghjkl;'#zxcvbnm,./     \n\n\n\n\n"
	m = dict((a,b) for a,b in zip(k[2:-2],k))

	ch = stdin.read(1)
	while len(ch):
		print(m[ch.lower()] , end='') 
		ch = stdin.read(1)
	
