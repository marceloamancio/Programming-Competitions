# UVA12554 - A Special "Happy Birthday" Song!!!  - Accepted
# goo.gl/rKTs3N
# @author: Marcelo Adriano Amancio
# 'Love the giver more than the gift.' --  Brigham Young

 
from sys import stdin
import math

if __name__ == '__main__':
    song = 'Happy birthday to you Happy birthday to you Happy birthday to Rujia Happy birthday to you'
    song = song.split()

    n = int(stdin.readline())
    people = []
    for _ in range(n):
        people.append(stdin.readline()[:-1])

    times_to_sing = math.ceil(len(people)/len(song))
    person_i = 0
    for _ in range(times_to_sing):
        for i in range(len(song)):
            print('%s: %s'%(people[person_i],song[i]))
            person_i = (person_i + 1) % len(people)
