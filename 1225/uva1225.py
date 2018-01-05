# UVA1225 - Digit Counting - Accepted
# goo.gl/S52PrN
# @author: Marcelo Adriano Amancio
# 'The best revenge is massive success.' -- Frank Sinatra

from sys import stdin

if __name__ == '__main__':
	n = int(stdin.readline())
	for i in range(0,n):
		v = [0]*10
		e = int(stdin.readline())
		for e in range(1,e+1):
			while e:
				v[e%10] += 1
				e = e//10
		for i in range(0,9):
			print (v[i],end=" ")
		print(v[9]) 




