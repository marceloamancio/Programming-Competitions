# UVA12289 - One-Two-Three - Accepted
# goo.gl/2U4rlk
# @author: Marcelo Adriano Amancio
# 'Do not confuse motion and progress. A rocking horse keeps moving but does not make any progress.' -- Alfred A. Montapert

from sys import stdin

if __name__ == '__main__':
	n = int(stdin.readline())
	for _ in range(n):
		line = stdin.readline()[:-1]
		if len(line) == 5:
			print(3)
		elif [ca == cb for ca,cb in zip(line, "one")].count(True) >=2:
			print(1)
		else:
			print(2)
		
		
