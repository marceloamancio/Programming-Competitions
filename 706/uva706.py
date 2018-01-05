# UVA706 - LC-Display - Accepted
# goo.gl/zp198J
# @author: Marcelo Adriano Amancio
# 'Always forgive your enemies; nothing annoys them so much.' -- Oscar Wilde


from sys import stdin

def print_any(n, a,b,c):
	print(a, end='')
	for i in range(0,n):
		print (b,end='')
	print(c, end='')

def print_hor(n,comb):
	ch = '-' if comb else ' '
	print_any(n, ' ', ch, ' ')

def print_ver(n,comb):
	a = '|' if comb//2 else ' ' 
	c = '|' if comb%2 else ' '
	print_any(n, a,' ', c)

def loop_hor(n, l, inp, x):
	ch = ''
	for e in inp:
		print(ch,end='')
		print_hor(n,l[e][x])
		ch = ' '
	print('')

def loop_ver(n, l, inp, x):
	for i in range(0,n):
		ch = ''
		for e in inp:
			print(ch,end='')
			print_ver(n,l[e][x])
			ch=' '
		print('')

if __name__ == '__main__':
	l = [[1,3,0,3,1], #0
	     [0,1,0,1,0], #1
	     [1,1,1,2,1], #2
	     [1,1,1,1,1], #3
	     [0,3,1,1,0], #4
	     [1,2,1,1,1], #5
	     [1,2,1,3,1], #6
	     [1,1,0,1,0], #7 
	     [1,3,1,3,1], #8
	     [1,3,1,1,1], #9
	]
	
	n, lv = stdin.readline().split()	

	while n!='0' or lv!='0':
		n = int(n)
		inp = [int(ch) for ch in lv]

		loop_hor(n,l,inp,0)
		loop_ver(n,l,inp,1)
		loop_hor(n,l,inp,2)
		loop_ver(n,l,inp,3)
		loop_hor(n,l,inp,4)
		print('')

		n, lv = stdin.readline().split()	


