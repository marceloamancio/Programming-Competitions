# UVA10038 - Jolly Jumpers - Accepted
# goo.gl/OGIJhC
# @author: Marcelo Adriano Amancio
# 'Acquaintance, n.: A person whom we know well enough to borrow from, but not well enough to lend to.' -- Ambrose Bierce


from sys import stdin

if __name__ == '__main__':
	line = stdin.readline()
	while line:
		l = [int(x) for x in line.split()]
		n = l[0]+1
		l[0] = l[1]
		rf = [False]*(n-1)
		for i in range(n-1):
			dif = abs(l[i+1] - l[i])
			if dif < n-1:
				rf[dif] = True
			else:
				break
		#print(l)		
		#print(rf,rf.count(False))
		if rf.count(False) == 0:
			print('Jolly')
		else:
			print ('Not jolly')
		
		
		line = stdin.readline()
	
