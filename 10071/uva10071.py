# UVA10071 - Back to High School Physics - Accepted
# goo.gl/2xonRf
# @author: Marcelo Adriano Amancio
# 'Those who believe in telekinetics, raise my hand.' -- Kurt Vonnegut

from sys import stdin

if __name__ == '__main__':
	x0, y0 = 0, 0
	line = stdin.readline()
	while len(line):
		x1, y1 = map(int,line.split())
		print( (2*y1+y0) * (x1-x0) ) 
		line = stdin.readline()
