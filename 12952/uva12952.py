# UVA12952 - Tri-du - Accepted
# goo.gl/Q0xmrB
# @author: Marcelo Adriano Amancio
# 'There is a great difference between worry and concern. A worried person sees a problem, and a concerned person solves a problem.' -- Harold Stephens


from sys import stdin

if __name__ == '__main__':
	line = stdin.readline()
	while line:
		a,b = map(int, line.split())
		print(max(a,b))
		line = stdin.readline()
	
