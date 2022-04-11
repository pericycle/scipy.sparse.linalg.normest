import numpy as np

def normest(M,tol):
    # return an approximation of the 2 norm of a matrix
    # M is a symmetric positive semi-definite numpy array or a scipy sparse matrix
    # up to a tolerance of tol using the power method
    max_it = 25
    res = 1
    it_count = 0
    x = np.random.rand(M.shape[1],1)
    y = M.dot(x)
    pnorm = np.sqrt(np.sum(y**2))
    x = y/pnorm
    while (res>tol)&(it_count<max_it):
        y = M.dot(x)
        ynorm = np.sqrt(np.sum(y**2))
        res = abs(pnorm-ynorm)
        x = y/ynorm
        it_count += 1
    v = M.dot(x)
    return np.sqrt(np.sum(v**2))
