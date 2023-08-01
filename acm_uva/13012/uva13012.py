# UVA13012 - Identifying tea - Accepted
# goo.gl/bJwa1Y
# @author: Marcelo Adriano Amancio
# 'It is easier to fight for one’s principles than to live up to them.' -- Alfred Adler


from sys import stdin

if __name__ == '__main__':
	line = stdin.readline()
	while line:
		n = int(line)
		v = [int(x) for x in stdin.readline().split()]		
		print(v.count(n))
		line = stdin.readline()
	
