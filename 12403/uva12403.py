# UVA12403 - Save Setu - Accepted
# goo.gl/F2Jq0s
# @author: Marcelo Adriano Amancio
# 'I don’t know the key to success, but the key to failure is trying to please everybody.' -- Bill Cosby


from sys import stdin

if __name__ == '__main__':
	n = int(stdin.readline())
	c =0
	for _ in range(n):
		line = stdin.readline()[:-1]
		if line == 'report':
			print(c)
		else:
			c += int(line.split()[1])
		
