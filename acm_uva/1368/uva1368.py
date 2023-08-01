# UVA1368 - DNA Consensus String - Accepted
# goo.gl/thZwdd
# @author: Marcelo Adriano Amancio
# 'For it is in giving that we receive'. -- Fancis of Assisi
from sys import stdin
from collections import Counter

gen_i = {'A':0,'C':1,'G':2,'T':3}
gen_a = ['A','C','G','T']

def rule_sort(x):
    return -10*x[0] + gen_i[x[1]]


def process_dna(k,size,dna_list):
    dna_consensus = []
    hamm_count = 0
    for i in range(size):
        j_list = [dna_list[j][i] for j in range(k)]
        counter = Counter(j_list)
        counter_list = sorted([(value,key) for key,value in counter.items()],key=rule_sort)

        dna_consensus.append(counter_list[0][1])
        hamm_count += (k-counter_list[0][0])


    return ''.join(dna_consensus),hamm_count


if __name__ == '__main__':
    n = int(stdin.readline())

    for _ in range(n):
        dna_list = []
        k, size = [int(x) for x in stdin.readline().split()]
        for _ in range(k):
            dna_list.append(stdin.readline()[:-1])

        a,b = process_dna(k,size,dna_list)
        print(a)
        print(b)

        None
    None
