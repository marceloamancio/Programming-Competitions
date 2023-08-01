# UVA10340 - All in All - Accepted
# goo.gl/mwTYqv
# @author: Marcelo Adriano Amancio
# 'If you're trying to create a company, it's like baking a cake. You have to have all the ingredients in the right proportion.' -- Elon Musk 

from sys import stdin

def subseq(a,b):
    la, lb = len(a) ,len(b)
    i, j = 0, 0
    if lb<la:
        return False

    while True:
        if i == la or j == lb:
            break

        if a[i] == b[j]:
            i+=1
        j+=1

    return i == la



if __name__ == '__main__':
    
    line = stdin.readline()
    while line:
        line = line[:-1].split()
        res = subseq(line[0], line[1])
        resa = 'Yes' if res else 'No'  
        print(resa)
        line = stdin.readline()
    None


