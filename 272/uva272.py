# UVA272 - TEX Quotes - Accepted
# goo.gl/VRKJqw
# @author: Marcelo Adriano Amancio
# 'Anyone who has never made a mistake has never tried anything new.' -- Albert Einstein

from sys import stdin

def main():
	begin_dq = True 
	v = {	begin_dq: "``", 
		not begin_dq: "''"}


	for line in stdin:
		for ch in line:
			if ch == '"':
				print (v[begin_dq],end="")
				begin_dq = not begin_dq 
			else:
				print (ch,end="")
			
main()

