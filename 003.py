#!/bin/usr/env python

#https://projecteuler.net/problem=3

#Largest prime factor

def prime_factors(n):
  "returns all prime factors of a positive int"
  factors = []
  d=2
  while n>1:
    while n%d==0:
      factors.append(d)
      n/=d
    d+=1
    #prime factors are at most sqrt(n)
    if d**2 > n:
      factors.append(n)
      break
  return factors

print max(prime_factors(600851475143))
