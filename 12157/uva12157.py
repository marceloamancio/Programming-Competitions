# UVA12157 -	Tariff Plan - Accepted
# goo.gl/qD9zjZ
# @author: Marcelo Adriano Amancio
# 'Mobile is a lot closer to TV than it is to desktop. ' -- Mark Zuckerberg


from sys import stdin

def price(call_len, max_t, price_interval):
    return price_interval * (1 + call_len%max_t)

if __name__ == '__main__':
    tc = int(stdin.readline())
    for i in range(tc):

        stdin.readline() #discard reading
        calls = [int(x) for x in stdin.readline().split()]

        price_mile = sum([10*(1+c//30) for c in calls])
        price_juice = sum([15*(1+c//60) for c in calls])
        lower_price = min(price_mile, price_juice)

        best_company = []
        if price_mile<=price_juice: best_company.append('Mile')
        if price_juice<=price_mile: best_company.append('Juice')
        best_company_name = ' '.join(best_company)

        print('Case %d: %s %d'%(i+1,best_company_name,lower_price))
