# UVA10082 - WERTYU - Accepted
# goo.gl/raD0Bn
# @author: Marcelo Adriano Amancio
# 'You could even say that the God of Genesis himself is a programmer: language, not manipulation, is his tool of creation. Words become worlds.' -- Pedro Domingos 


from sys import stdin

kb = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./   "

if __name__ == '__main__':
	m={}
	for i in range(1,len(kb)):
		m[kb[i]] = kb[i-1]
	
	line = stdin.readline()[:-1]
	while line:
		res = ''.join([m[x] for x in line])
		print(res)
		line = stdin.readline()[:-1]
