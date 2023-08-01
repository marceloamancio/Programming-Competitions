# UVA1727 - Counting Weekend Days - Accepted
# goo.gl/55XInf
# @author: Marcelo Adriano Amancio
# 'Before I got married I had six theories about bringing up children; now I have six children and no theories.' -- John Wilmot


from sys import stdin

if __name__ == '__main__':
	n = int(stdin.readline())
	m = {	'JAN': 3, 'FEB':0, 'MAR':3, 'APR':2, 'MAY':3, 'JUN':2, 
	  	'JUL':3 , 'AUG':3, 'SEP':2, 'OCT':3, 'NOV':2, 'DEC':3}
	d = {'SUN':0, 'MON':1, 'TUE':2, 'WED':3, 'THU':4, 'FRI':5, 'SAT':6 }
	week_c = [0,0,0,0,0,1,1]
	for ii in range(0,n):
		month, day = stdin.readline().split()	
		c = 0 
		for i in range(0,m[month]):
			c+= week_c[ (d[day] + i) % 7]
		print(8+c)
		
