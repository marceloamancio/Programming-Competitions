# UVA10018 - Reverse and Add - Accepted
# goo.gl/Ma5h7z
# @author: Marcelo Adriano Amancio
# 'What I cannot create, I do not understand.' -- Richard Feynman


from sys import stdin

if __name__ == '__main__':
	n = int(stdin.readline())
	for _ in range(n):
		e = int(stdin.readline())

		cc = 0
		while True:
			se = str(e)
			re = se[::-1]
			if se == re:
				break
			e = int(se) + int(re)
			cc += 1
		print(cc, e)
		

