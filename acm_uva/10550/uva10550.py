# UVA10550 - Combination Lock - Accepted
# goo.gl/OZwFGg
# @author: Marcelo Adriano Amancio
# 'The cure for boredom is curiosity. There is no cure for curiosity.' -- Ellen Parr
from sys import stdin

if __name__ == '__main__': 
	p, a,b,c = map(int,stdin.readline().split())	
	while p+a+b+c:
		ft = 2*40 				#step 1
		ft += p - a if a<p else 40-a+p 		#step 2
		ft += 40 				#step 3
		ft += b - a if b>a else 40+b-a 		#step 4
		ft += b - c if c<b else 40-c+b		#step 5
		
		print(9*ft)	
		p, a,b,c = map(int,stdin.readline().split())	
