# UVA12015 - Google is Feeling Lucky - Accepted
# goo.gl/zGdaT7
# @author: Marcelo Adriano Amancio
# 'Never ascribe to malice, that which can be explained by incompetence.' -- Napoleon (Hanlon’s Razor)


from sys import stdin

if __name__ == '__main__':
	n = int(stdin.readline())
	ci = 1
	for _ in range(0,n):
		br = -1
		q = []
		for _ in range(0,10):
			site, r = stdin.readline().split() 
			r = int(r)
			if r>br:
				q = [site]
				br = r
			elif r==br:
				q.append(site)
		print('Case #{}:'.format(ci))
		ci+=1
		for e in q:
			print (e)
