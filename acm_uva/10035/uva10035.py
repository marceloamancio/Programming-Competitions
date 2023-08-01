# UVA10035 - Primary Arithmetic - Accepted
# goo.gl/NwwuvQ
# @author: Marcelo Adriano Amancio
# 'People worry that computers will get too smart and take over the world, but the real problem is that they're too stupid and they've already taken over the world.' -- Pedro Domingos 


from sys import stdin

if __name__ == '__main__':
	a,b = map(int, stdin.readline().split())
	while a+b:
		carry = 0
		cc = 0

		while a or b:
			carry = (carry + a%10 + b%10)//10
			if carry:
				cc += 1
			a = a//10
			b = b//10

		if cc == 0:
			print('No carry operation.')
		elif cc == 1:
			print('1 carry operation.')
		else:
			print('{} carry operations.'.format(cc))
			 		

		a,b = map(int, stdin.readline().split())
	
