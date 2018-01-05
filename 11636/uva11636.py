# UVA11636 - Hello World! - Accepted
# goo.gl/FhR44v
# @author: Marcelo Adriano Amancio
# 'People often say that motivation doesn’t last. Well, neither does bathing – that’s why we recommend it daily.' -- Zig Ziglar



from sys import stdin
from bisect import bisect

if __name__ == '__main__':
	l = [2**x for x in range(0,15)]
	e = int(stdin.readline())
	c = 1
	while e > 0:
		print('Case {}: {}'.format(c,bisect(l,e-1)))
		c+=1
		e = int(stdin.readline())

	
