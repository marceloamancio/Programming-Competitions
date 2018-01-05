# UVA11727 - Cost Cutting - Accepted
# goo.gl/xgPQfu
# @author: Marcelo Adriano Amancio
# 'If you don’t make mistakes, you’re not working on hard enough problems. And that’s a big mistake.' -- Frank Wilczek


from sys import stdin

if __name__ == '__main__': 
	n = int(stdin.readline())	
	i = 1
	for _ in range(n):
		a,b,c = map(int, stdin.readline().split())
		r =sorted([a,b,c])[1]
		print("Case {}: {}".format(i,r))
		i += 1
