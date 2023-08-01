# UVA264 - Count on Cantor - Accepted
# t.ly/L8pNn
# @author: Marcelo Adriano Amancio
# 'Every artist was first an amateur.' -- Ralph Waldo Emerson


from sys import stdin

def sum_inv(d):
  import math
  d = d-1
  return  math.floor(1. + (-1. + math.sqrt(1 + 8*d)) / 2.)

def ne_triangle(a):
  return int(a + ((a*a - a) / 2))


def process(n):
  d = sum_inv(n)
  ne = ne_triangle(d-1)
  j = n - ne - 1

  a = 1 + j
  b = d - j

  if d%2:
    a,b = b,a
  return a,b


if __name__ == '__main__':
  for line in stdin:
    line = int(line.strip())
    print("TERM {} IS {}/{}".format(line, *process(line)))

