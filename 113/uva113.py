# UVA113 - Power of Cryptography - Accepted
# goo.gl/X8rDnJ
# @author: Marcelo Adriano Amancio
#'Adding sound to movies would be like putting lipstick on the Venus de Milo.' -- Mary Pickford

from sys import stdin
from math import pow

if __name__ == '__main__':
	line = stdin.readline()
	while line:
		n = int(line)
		p = int(stdin.readline())
		print(int(round(pow(p,1/n),0)))
	
		line = stdin.readline()

				
	 
		
