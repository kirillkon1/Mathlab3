import math
from abc import ABC, abstractmethod
from Functions import AbstractFunction

import private as private


class AbstractMethod(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def solve(self, fun: AbstractFunction, n=-1) -> float:
        pass

    @abstractmethod
    def find_n(self, fun: AbstractFunction, eps: float) -> int:
        pass

    def __str__(self) -> str:
        return "AbstractMethod"


class RectangleMethod(AbstractMethod):

    def __init__(self, mode: int) -> None:
        super().__init__()
        if 1 <= mode <= 3:
            self.mode = mode
        else:
            self.mode = 3

    def solve(self, fun: AbstractFunction, n=-1, rupture=False) -> float:

        h = (fun.b - fun.a) / n

        # i separated it into to integrals
        if (fun.__str__() == 'sin(x)/x' or fun.__str__() == '1/(x-2)') and not rupture:
            if fun.a < fun.getPoint() < fun.b:
                fun1 = fun
                fun1.b = fun.getPoint() - 0.0001
                fun2 = fun
                fun2.a = fun.getPoint() + 0.0001
                return self.solve(fun1, n, True) + self.solve(fun2, n, True)

        if self.mode == 1:
            return self.__leftMode(fun, n)
        elif self.mode == 2:
            return self.__rightMode(fun, n)
        else:
            return self.__centerMode(fun, n)

    @staticmethod
    def __leftMode(fun: AbstractFunction, n: int):
        a, b = fun.a, fun.b
        h = (b - a) / n
        i = 0
        for j in range(n - 1):
            i += fun.find(a + (j - 1) * h)

        return i * h

    @staticmethod
    def __rightMode(fun: AbstractFunction, n: int):
        a, b = fun.a, fun.b
        h = (b - a) / n
        i = 0
        for j in range(n):
            i += fun.find(a + j * h)

        return i * h

    @staticmethod
    def __centerMode(fun: AbstractFunction, n: int):
        a, b = fun.a, fun.b
        h = (b - a) / n
        i = 0

        for j in range(1, n):
            i += fun.find(a + h / 2 + j * h)
        return i * h

    def find_n(self, fun: AbstractFunction, eps: float) -> int:
        tmp = int(math.pow(
            max(abs(fun.getSecondDerivative(fun.a)), abs(fun.getSecondDerivative(fun.b))) * math.pow((fun.b - fun.a),
                                                                                                     3) / (
                    24 * eps), 1 / 2))

        return tmp + 1 if tmp % 2 == 1 else tmp + 2

    def __str__(self) -> str:
        return "RectangleMethod"


class TrapezoidMethod(AbstractMethod):

    def __init__(self) -> None:
        super().__init__()

    def solve(self, fun: AbstractFunction, n=10, rupture=False) -> float:
        a, b = fun.a, fun.b

        h = (b - a) / n
        i = fun.find(a) / 2 + fun.find(b) / 2

        if (fun.__str__() == 'sin(x)/x' or fun.__str__() == '1/(x-2)') and not rupture:
            if fun.a < fun.getPoint() < fun.b:
                fun1 = fun
                fun1.b = fun.getPoint() - 0.0001
                fun2 = fun
                fun2.a = fun.getPoint() + 0.0001
                return self.solve(fun1, n, True) + self.solve(fun2, n, True)

        for j in range(1, n):
            i = i + fun.find(a + j * h)

        return i * h

    def find_n(self, fun: AbstractFunction, eps: float) -> int:
        tmp = int(math.pow(
            max(abs(fun.getSecondDerivative(fun.a)), abs(fun.getSecondDerivative(fun.b))) * math.pow((fun.b - fun.a),
                                                                                                     3) / (
                    12 * eps), 0.5))

        return tmp + 1 if tmp % 2 == 1 else tmp + 2

    def __str__(self) -> str:
        return "TrapezoidMethod"


class SimpsonMethod(AbstractMethod):

    def __init__(self) -> None:
        super().__init__()

    def solve(self, fun: AbstractFunction, n=-1, rupture=False) -> float:
        a, b = fun.a, fun.b
        h = (b - a) / n

        if (fun.__str__() == 'sin(x)/x' or fun.__str__() == '1/(x-2)') and not rupture:
            if fun.a < fun.getPoint() < fun.b:
                fun1 = fun
                fun1.b = fun.getPoint() - 0.0001
                fun2 = fun
                fun2.a = fun.getPoint() + 0.0001
                return self.solve(fun1, n, True) + self.solve(fun2, n, True)

        i_odd = 0
        i_even = 0
        i = fun.find(a) + fun.find(b)
        for j in range(1, n - 1):
            if j % 2 == 0:
                i_even += fun.find(a + h * j)
            else:
                i_odd += fun.find(a + h * j)
        return (i + 4 * i_odd + 2 * i_even) * h / 3

    def find_n(self, fun: AbstractFunction, eps: float) -> int:
        tmp = int(math.pow(
            max(abs(fun.getFourthDerivative(fun.a)), abs(fun.getFourthDerivative(fun.b))) * math.pow((fun.b - fun.a),
                                                                                                     5) / (
                    12 * eps), 1 / 4))

        return tmp + 1 if tmp % 2 == 1 else tmp + 2

    def __str__(self) -> str:
        return "SimpsonMethod"


def find_Rn(fun: AbstractFunction, n=10):
    if fun.__str__() == "RectangleMethod":
        x = max(fun.getSecondDerivative(fun.a), fun.getSecondDerivative(fun.b))
        return x * (fun.b - fun.a) ** 3 / (24 * n ** 2)
    if fun.__str__() == "TrapezoidMethod":
        x = max(fun.getSecondDerivative(fun.a), fun.getSecondDerivative(fun.b))
        return x * (fun.b - fun.a) ** 3 / (12 * n ** 2)
    if fun.__str__() == "SimpsonMethod":
        x = max(fun.getFourthDerivative(fun.a), fun.getSecondDerivative(fun.b))
        return x * (fun.b - fun.a) ** 5 / (180 * n ** 4)
