# UVA10370 - Above Average - Accepted
# goo.gl/wWbZQY
# @author: Marcelo Adriano Amancio
# 'Sometimes I worry about being a success in a mediocre world.' -- Lily Tomlin
from sys import stdin

if __name__ == '__main__':
	cc = int(stdin.readline())
	for i in range(0,cc):
		l =  [int(e) for e in stdin.readline().split()]
		avg = sum(l[1:])/l[0]
		s = [1 if x>avg else 0 for x in l[1:]]
		r = sum(s)/len(s)
		print ("%.3f%%"%(r*100))
		
		
		 
