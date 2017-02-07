import numpy as np
import random

def check_rep(n):
	num = random.randint(1, n)
	print "Expected num is %d" % num 
	d = np.zeros(n+1, dtype=np.int32)
	for i in range(n):
		d[i] = i+1
	d[n] = num
	sum = 0
	for i in range(n+1):
		sum += d[i]
	print sum
	sum_2 = n*(n+1)/2
	print sum_2
	num_check = sum - sum_2
	print "We got %d" % num_check