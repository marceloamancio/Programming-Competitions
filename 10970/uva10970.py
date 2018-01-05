# UVA10970 - Big Chocolate - Accepted
# goo.gl/ObbBP8
# @author: Marcelo Adriano Amancio
# 'The real voyage of discovery consists not in seeking new lands but seeing with new eyes.' -- Marcel Proust


from sys import stdin

if __name__ == '__main__':
	line = stdin.readline()
	while len(line):
		m,n = map(int, line.split())
		print((m-1)+m*(n-1))
		line = stdin.readline()

