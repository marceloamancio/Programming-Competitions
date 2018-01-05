# UVA10055 - Hashmat the Brave Warrior - Accepted
# goo.gl/1FBHLl
# @author: Marcelo Adriano Amancio
# 'We build too many walls and not enough bridges.' -- Isaac Newton


from sys import stdin

def main():
	for line in stdin:
		a,b = [int(s) for s in line.split()]
		print(max(a,b)-min(a,b))

main()

