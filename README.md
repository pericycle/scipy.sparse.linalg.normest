# scipy.sparse.linalg.normest
This short code returns an estimate of the spectral norm of a scipy sparse matrix in csr format.
The spectral norm of a scipy sparse matrix is not implemented in the current version of scipy.
normest uses the power iteration to compute the largest eigenvalue.

Example:
from scipy.sparse import rand
A = rand(1000,1000, density = 0.01, format = 'csr')
B = A.T.dot(A)
tol = 1e-4
est = normest(A,tol)
