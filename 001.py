#!/bin/usr/env python
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
  
def naive(n):
  # O(n) runtime
  sum=0
  for k in xrange(n):
    if k%3==0 or k%5==0: sum+=k
  return sum
  
def best(n):
  # O(1) runtime
  SumMultsOf3=sumDivByN(n,3)
  SumMultsOf5=sumDivByN(n,5)
  SumMultsOf15=sumDivByN(n,15)
  return SumMultsOf3+SumMultsOf5-SumMultsOf15
  
def sumDivByN(n,k):
  t=n/k
  return k*(t*(t+1)/2)
  
if __name__ == '__main__':
  print best(1000)
