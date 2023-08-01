# UVA591 - Box of Bricks - Accepted
# goo.gl/oXl6ve
# @author: Marcelo Adriano Amancio
# 'Being second is to be the first of the ones who lose.' -- Ayrton Senna


from sys import stdin

def main():
	c = 1
	for nstr in stdin:
		n = int(nstr)
		if n==0:
			break
		
		elems = [int(x) for x in stdin.readline().split()]
		sume = sum(elems)
		avg = sume//n
		ans = sum([e-avg for e in elems if (e-avg) > 0]) 


		print("Set #{}".format(c))
		print("The minimum number of moves is {}.\n".format(ans))
		c+=1
			

main()
