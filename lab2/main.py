import numpy as np

n = 20
c = 3
p = 21
teta10 = [2, 2, 4, 2, 5, 3, 5, 7, 3, 2]

T_c_s = np.sum(teta10)
print("T_c_s =", T_c_s)
sigma = np.sqrt(np.math.floor(n/c))
print("sigma =", sigma)


def f(x) -> int:
    return (np.math.floor(n/c) - 1)*T_c_s*((x - 1)/x)*(x + np.math.floor(n/c) - 1)


def tau_estimation(sigma_):
    if type(sigma_) == int:
        estimation = f(1 + sigma_)
    else:
        estimation = max(f(1 + np.math.floor(sigma_)), f(2 + np.math.floor(sigma_)))
    return estimation


print("tau <=", tau_estimation(sigma))
