# UVA11332 - Summing Digits - Accepted
# goo.gl/UavnzS
# @author: Marcelo Adriano Amancio
# 'If you have God on your side, everything becomes clear..' -- Ayrton Senna


from sys import stdin

def main():
	s = 0
	lastch = "^"
	l = 0
	while True:
		ch = stdin.read(1)
		if ch == '\n' and lastch == '0' and l==1:		
			break
		elif ch == '\n' : 
			s = s%10 + s//10	
			print(s)
			s = 0
			lastch = '^'
			l=0
		else:
			i = ord(ch)-ord('0') + s
			s = i%10 + i//10	
			l = l+1
			lastch = ch

main()
