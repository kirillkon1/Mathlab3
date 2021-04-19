import sys

from Functions import *
from Utils import userRead, toFixed, drawImage

if __name__ == '__main__':
    fun, eps, method, mode = userRead()
    n = 2
    # drawImage(fun)

    res = method.solve(fun, n)
    res_prev = method.solve(fun, int(n / 2))
    while abs(res - res_prev) > eps:
        n *= 2
        res_prev = res
        res = method.solve(fun, n)
        if n > 10000000:
            print("Нельзя найти ответ")
            sys.exit()

    print(f"Ответ: {toFixed(res, -int(np.log10(eps)) * 2)} ± {toFixed(eps, -int(np.log10(eps)))}")
    print(f"\nИнтеграл: {fun}, \nМетод: {method}, \nКол-во делений: {n} ")
