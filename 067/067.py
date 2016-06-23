#!/usr/bin/env python

#https://projecteuler.net/problem=67

'''Similar to p18'''

import time 
start = time.time()

with open("p067_triangle.txt","r") as fn:
	raw_data=fn.read()
	a = raw_data.split("\n")
	new_a = [x.split(" ") for x in a] 
	
	del new_a[-1]

	new_a=[map(int,k) for k in new_a]
	new_a.reverse()
	sum=0
	for k in xrange(len(new_a)):
		i=0
		while i+1<len(new_a[k]) and k+1 in xrange(len(new_a)):
			add=max(new_a[k][i],new_a[k][i+1])
			new_a[k+1][i]+=add
			i+=1

	print new_a[-1][0]
	print 'It took', time.time()-start, 'seconds.'