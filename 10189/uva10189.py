# UVA10189 - Minesweeper - Accepted
# goo.gl/7DRNwN
# @author: Marcelo Adriano Amancio
# 'Try not to become a man of success, but rather try to become a man of value..' -- Albert Einstein

from sys import stdin

MAXN = 105

def add_dot(ii,jj, mat):
	mat[ii][jj] = '*'

	for i in range(ii-1,ii+2): 	
		for j in range(jj-1,jj+2):
			if (mat[i][j] != '*'):
				mat[i][j]+=1 	


			
def print_mat(m,n,mat):
	for i in range(1,m+1):
		for j in range(1,n+1):
			print(mat[i][j],end="")
		print("")


def main():
	counter = 1
	#for each input
	for line in stdin:
		#create zero matrix and read input
		mat = [[0 for x in range(MAXN)] for y in range(MAXN)] 
		m, n = [int (s) for s in line.split()]
		if(m*n == 0):
			break 

		#print answer header
		if counter != 1:
			print ("")
		print("Field #{}:".format(counter))
		counter+=1


		for i in range(1,m+1):
			l = stdin.readline()
		
			#for each mine matrix line
			for j in range(0,n):
				if l[j] == '*':
					add_dot(i,j+1,mat)
		print_mat (m,n,mat)

main()
