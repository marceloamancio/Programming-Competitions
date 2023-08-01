# UVA11364 - Parking - Accepted
# goo.gl/4s9Pzw
# @author: Marcelo Adriano Amancio
# 'An inventor is simply a fellow who doesn’t take his education too seriously.' -- Charles F. Kettering


from sys import stdin

if __name__ == '__main__': 
	n = int(stdin.readline())
	for _ in range(n):
		p = int(stdin.readline())
		v = [int(e) for e in stdin.readline().split()]
		print(2*(max(v)-min(v)))
