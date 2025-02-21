import numpy as np

def secante(f, x0, x1, N, tol):
    iterations = np.array([x0])
    iterations = np.append(iterations,f(x0))
    n = 1
    eps = np.finfo(np.float64).eps
    err_rel = np.abs(iterations[n]-iterations[n-1])/(np.abs(iterations[n])+eps)
    while (err_rel >= tol and n < N):
        iterations = np.append(iterations,f(iterations[n]))
        err_rel = np.abs(iterations[n+1]-iterations[n])/(np.abs(iterations[n+1])+eps)
        n += 1
    return iterations