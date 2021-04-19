import math
import sys
from abc import ABC, abstractmethod

import numpy as np


class AbstractFunction(ABC):
    def __init__(self, a: float, b: float) -> None:
        super().__init__()
        self.a = a
        self.b = b

    def __str__(self) -> str:
        return super().__str__()

    @abstractmethod
    def find(self, x) -> float:
        return 0

    @abstractmethod
    def getSecondDerivative(self, x: float) -> float:
        return 0

    @abstractmethod
    def getFourthDerivative(self, x: float) -> float:
        return 0

    @abstractmethod
    def getPoint(self):
        pass


# integral (4x^3 - 5x^2 + 6x - 7)dx x = 0..2
# answer: 2/3 ~= 0.666667
class TheFirstFunction(AbstractFunction):

    def __init__(self, a: float, b: float) -> None:
        super().__init__(a, b)

    def __str__(self) -> str:
        return f"4x^3 - 5x^2 + 6x - 7)dx x = {self.a}..{self.b}"

    def find(self, x) -> float:
        return 4 * x ** 3 - 5 * x ** 2 + 6 * x - 7

    def getSecondDerivative(self, x: float) -> float:
        return 24 * x - 10

    def getFourthDerivative(self, x: float) -> float:
        return 0

    def getPoint(self):
        return 'not'


# integral (3^(x/3) + x/3 + 3)dx x = -3..3
# answer: 25.282
class TheSecondFunction(AbstractFunction):

    def __init__(self, a: float, b: float) -> None:
        super().__init__(a, b)

    def __str__(self) -> str:
        return f"(3^(x/3) + x/3 + 3)dx x = {self.a}..{self.b}"

    def find(self, x) -> float:
        return 3 ** (x / 3) + x / 3 + 3

    # 3^(x/3 - 2) * ln^2(3)
    def getSecondDerivative(self, x: float) -> float:
        return pow(3, x / 3 - 2) * np.log(3) ** 2

    # 3^(x/3 - 4) * ln^4(3)
    def getFourthDerivative(self, x: float) -> float:
        return pow(3, x / 3 - 4) * np.log(3) ** 4

    def getPoint(self):
        return 'not'


# integral (ln(3x) + 3)dx x = 1..7
# answer: 32.213
class TheThirdFunction(AbstractFunction):

    def __init__(self, a: float, b: float) -> None:
        super().__init__(a, b)

    def __str__(self) -> str:
        return f"(ln(3x) + 3)dx x = {self.a}..{self.b}"

    def find(self, x) -> float:
        if x < 0:
            print("выход за пределы ОДЗ")
            sys.exit()
        return np.log(3 * x) + 3

    # -1/x^2
    def getSecondDerivative(self, x: float) -> float:
        return -1 / (x ** 2)

    # -6/x^4
    def getFourthDerivative(self, x: float) -> float:
        return -6 / (x ** 4)

    def getPoint(self):
        return 'not'


class TheFourthFunction(AbstractFunction):

    def __init__(self, a: float, b: float) -> None:
        super().__init__(a, b)

    def __str__(self) -> str:
        return "1/(x-2)"

    def find(self, x) -> float:
        if x == 2:
            x += 0.00001
        result = 1 / (x - 2)
        return result

    def getSecondDerivative(self, x: float) -> float:
        return 2 / pow(x - 2, 3)

    def getFourthDerivative(self, x: float) -> float:
        return 24 / pow(x - 2, 5)

    def getPoint(self):
        return 2


class TheFifthFunction(AbstractFunction):
    def __init__(self, a: float, b: float) -> None:
        super().__init__(a, b)

    def __str__(self) -> str:
        return "sin(x)/x"

    def find(self, x: float) -> float:
        if x == 0:
            x += 0.00001
        result = math.sin(x) / x
        return result

    # don't use bcs it is not really needed
    def getSecondDerivative(self, x: float) -> float:
        return 1

    def getFourthDerivative(self, x: float) -> float:
        return 1

    def getPoint(self):
        return 0
