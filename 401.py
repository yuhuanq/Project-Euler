#!/usr/bin/env python

#p401

''' Sum of squares of divisors

The divisors of 6 are 1,2,3 and 6.
The sum of the squares of these numbers is 1+4+9+36=50.

Let sigma2(n) represent the sum of the squares of the divisors of n. Thus sigma2(6)=50.
Let SIGMA2 represent the summatory function of sigma2, that is SIGMA2(n)=SUM(sigma2(i)) for i=1 to n.
The first 6 values of SIGMA2 are: 1,6,16,37,63 and 113.

Find SIGMA2(1015) modulo 109.
'''

import time
start = time.time()

def factors(n):
	# Returns set of all factors of n. O(sqrt(n)) runtime.
	result=set()
	sqrtn=int(n**.5)
	for k in range(1,sqrtn+1):
		q,r=n/k,n%k
		if r==0: result.add(q);result.add(k)
	return result

def sigma2(n):
	facs=factors(n)
	squares=[i**2 for i in facs]
	return sum(squares)

def SIGMA2(n):
	sum=0
	for k in xrange(1,n+1):
		sum+=sigma2(k)
	return sum

if __name__ == '__main__':
	print SIGMA2(6)
	print sigma2(1),sigma2(2),sigma2(3),sigma2(4),sigma2(5),sigma2(6)
	print SIGMA2(10**15)%10**9

print "It took", time.time()-start, "seconds."