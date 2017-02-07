from timeit import timeit

import numcheck
import numc_cython

N = 1

print "*" * 80
print "python check_rep(): %.10f" % timeit("check_rep(100)",
                                           "from numcheck import check_rep",
                                           number=N)

print "cython check_rep(): %.10f" % timeit("check_rep(100)",
                                           "from numc_cython import check_rep",
                                           number=N)

print "*" * 80