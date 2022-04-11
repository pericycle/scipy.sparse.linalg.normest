# scipy.sparse.linalg.normest
This short code returns an estimate of the spectral norm of a scipy sparse matrix in csr format.
The spectral norm of a scipy sparse matrix is not implemented in the current version of scipy.

Example:

import numpy as np
from scipy.sparse import rand

A = rand(1000,1000,density=0.01, format='csr')
tol = 1e-4
twonorm = normest(A,tol)
