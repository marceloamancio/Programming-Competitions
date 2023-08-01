# UVA12250 - Language Detection - Accepted
# goo.gl/XtSf26
# @author: Marcelo Adriano Amancio
# 'You can never get enough of what you don’t really need.' -- Eric Hoffer

from sys import stdin

if __name__ == '__main__':

	m = { 	'HELLO':'ENGLISH', 
		'HOLA':'SPANISH', 
		'HALLO':'GERMAN' ,
		'BONJOUR':'FRENCH',
		'CIAO':'ITALIAN' ,
		'ZDRAVSTVUJTE' :'RUSSIAN'}

	nc = 1
	while True:
		line = stdin.readline()[:-1]
		if line == '#':
			break 

		ans = m[line] if (line in m) else 'UNKNOWN'  
		print ('Case {}: {}'.format(nc, ans))
		nc += 1
	
