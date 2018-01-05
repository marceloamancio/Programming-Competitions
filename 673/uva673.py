# UVA673 - Parentheses Balance - Accepted
# goo.gl/rN6EzX
# @author: Marcelo Adriano Amancio
# 'When you are fitted in a racing car and you race to win, second or third place is not enough..' -- Ayrton Senna

from sys import stdin

def main():
	n = int(stdin.readline())

	for i in range(0,n):
		correct = True

		l = []
		match={']':'[', ')':'('}
		line = stdin.readline()[0:-1]
		for c in line:
			if c in "[(":
				l.append(c)
			elif len(l) == 0:
				correct = False
				break
			elif l.pop() != match[c]:
				correct = False
				break
		if len(l):
			correct = False	
		
		if correct:
			print("Yes")
		else:
			print("No")

main()
