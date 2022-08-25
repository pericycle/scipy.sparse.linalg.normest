# scipy.sparse.linalg.normest
This short code returns an estimate of the spectral norm of a symmetric positive semi-definite scipy sparse matrix.
The spectral norm of a scipy sparse matrix is not implemented in the current version of scipy. (SciPy v 1.9.0)
normest uses the power iteration to compute the largest eigenvalue.

# Example:
from scipy.sparse import rand <br/>
A = rand(1000,1000, density = 0.01, format = 'csr') <br/>
B = A.T.dot(A) <br/>
est = normest(B) <br/>
print('normest approximation: ', est) <br/> 

# compare with output from numpy.linalg.norm  <br/>

import numpy as np <br/>
C = B.todense() <br/>
est1 = np.linalg.norm(C, ord=2) <br/>
print('np.linalg.norm approximation: ', est1) <br/>
error = np.abs(est-est1) <br/>
print('Error: ', error) <br/>
