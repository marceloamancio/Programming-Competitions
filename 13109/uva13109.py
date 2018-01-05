# UVA13109 - Elephants - Accepted
# goo.gl/S3DRC9
# @author: Marcelo Adriano Amancio
# 'Look, there's no metaphysics on earth like chocolates.' -- Fernando Pessoa


from sys import stdin

if __name__ == '__main__':
	n = int(stdin.readline())
	for ii in range(0,n):
		m,w = map(int, stdin.readline().split())	
		l = sorted([int (x) for x in stdin.readline().split()])

		s = 0
		nelefs = m
		for i in range(0,m):
			if s + l[i] > w:
				nelefs = i
				break
			s += l[i]
		print(nelefs)
		
