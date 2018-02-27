# UVA119 - Greedy Gift Givers - Accepted
# goo.gl/5uHz7Q
# @author: Marcelo Adriano Amancio
# "It's one of the greatest gifts you can give yourself, to forgive. Forgive everybody." --  Maya Angelou

from sys import stdin

if __name__ == '__main__':

    n_line = stdin.readline()
    first_line = True
    while n_line:
        if first_line:
            first_line = False
        else:
            print()

        names = stdin.readline()[:-1].split()
        m_netv = {}
        for n in names: m_netv[n] = 0
        for _ in range(int(n_line)):
            row = stdin.readline()[:-1].split()
            v,p = int(row[1]), int(row[2])
            giver = row[0]
            receivers = row[3:]

            if p!=0:
                m_netv[giver] += v%p - v
            for r in receivers:
                if p!=0:
                    m_netv[r] += v//p

        for name in names:
            print(name,m_netv[name])

        n_line = stdin.readline()
    None
