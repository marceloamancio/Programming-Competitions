# UVA12279 - Emoogle Balance - Accepted
# goo.gl/zGSHLY
# @author: Marcelo Adriano Amancio
# 'Insanity: doing the same thing over and over again and expecting different results.' -- Albert Einstein 


from sys import stdin

if __name__ == '__main__':
	nc = 1
	while True:
		n = int(stdin.readline())
		if n == 0:
			break
			
		l = [int(x) for x in stdin.readline().split()]	
		zeros = l.count(0)
		others = len(l) - zeros
		print('Case {}: {}'.format(nc, others-zeros) )
		nc+=1
		
