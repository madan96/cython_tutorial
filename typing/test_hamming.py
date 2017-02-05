from timeit import timeit


print "*" * 80
print "python hamming_sum(): %.2f" % timeit('hamming_sum("qasdf","asdfa")','from hamming import hamming_sum')

print "cython hamming_sum(): %.2f" % timeit('hamming_sum("qasdf","asdfa")','from hamming_cython import hamming_sum')

print "optimal hamming_sum(): %.2f" % timeit('hamming_sum("qasdf","asdfa")','from hamming_cython_solution import hamming_sum')

print "=" * 80
print "python hamming_loop(): %.2f" % timeit('hamming_loop("qasdf","asdfa")','from hamming import hamming_loop')

print "cython hamming_loop(): %.2f" % timeit('hamming_loop("qasdf","asdfa")','from hamming_cython import hamming_loop')

print "optimal hamming_loop(): %.2f" % timeit('hamming_loop("qasdf","asdfa")','from hamming_cython_solution import hamming_loop')
