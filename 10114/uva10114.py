# UVA10114-  Loansome Car Buyer - Accepted
# goo.gl/zrBkrc
# @author: Marcelo Adriano Amancio
# "I couldn't find the sports car of my dreams, so I built it myself. " -- Ferdinand Porsche

from sys import stdin

if __name__ == '__main__':
    while True:
        ml,dp,lo,nd = [float(x) for x in stdin.readline().split()]
        ml,nd = int(ml), int(nd)
        if ml<0: break

        dep_r = []
        for i in range(nd):
            mo, pc = [float(x) for x in stdin.readline().split()]
            mo = int(mo)
            dep_r.append((mo,pc))
        dep_r = list(reversed(dep_r))

        car_price = lo + dp

        dp_i = None
        monthly_pay = lo/ml
        for i in range(ml+1):
            #update depreciation month
            if len(dep_r) > 0:
                if dep_r[-1][0] == i:
                    dp_i = dep_r[-1][1]
                    del dep_r[-1]

            #apply depreciarion
            car_price = car_price * (1-dp_i)

            #calc loan
            if i!=0:
                lo -= monthly_pay

            if lo<car_price:
                print(i,'month' + ('s' if i!=1 else ''))
                break
