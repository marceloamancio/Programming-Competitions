# UVA102 - Ecological Bin Packing - Accepted
# goo.gl/kcLes0
# @author: Marcelo Adriano Amancio
# 'Discipline is the bridge between goals and accomplishment.' -- Jim Rohn 


from sys import stdin

if __name__ == '__main__':
	line = stdin.readline()
	while line:
		b1,g1,c1, b2,g2,c2, b3,g3,c3 = map(int, line.split())
		mb1, mb2, mb3 = b2+b3, b1+b3, b1+b2 
		mg1, mg2, mg3 = g2+g3, g1+g3, g1+g2 
		mc1, mc2, mc3 = c2+c3, c1+c3, c1+c2 
		m = {
			'BCG': mb1 + mc2 + mg3,
			'BGC': mb1 + mg2 + mc3,
			'CGB': mc1 + mg2 + mb3,
			'CBG': mc1 + mb2 + mg3,
			'GCB': mg1 + mc2 + mb3,
			'GBC': mg1 + mb2 + mc3,
		}
		minim = m['BCG']
		s = 'BCG'
		for k,v in m.items():
			if v==minim and k<s:
				s = k
			elif v<minim:
				minim=v
				s = k
	
		print(s,minim)	

		line = stdin.readline()
