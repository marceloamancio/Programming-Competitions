# UVA11292 - Dragon of Loowater - Accepted
# goo.gl/yf9p6m
# @author: Marcelo Adriano Amancio
# 'I don’t deserve this award, but I have arthritis and I don’t deserve that either.' -- Jack Benny


from sys import stdin

if __name__ == '__main__':
	n,m = map(int, stdin.readline().split())
	while n+m:
		ln = sorted([int(stdin.readline()) for _ in range(n)],reverse=True)
		lm = sorted([int(stdin.readline()) for _ in range(m)],reverse=True)
		doomed = True
		c = 0
		while len(lm)>=len(ln):
			knight = lm.pop()
			if(knight>=ln[-1]):
				ln.pop()	
				c+=knight
			if(len(ln) == 0):
				doomed = False
				break
			
		if doomed:
			print('Loowater is doomed!')
		else:
			print(c)
		
		n,m = map(int, stdin.readline().split())
