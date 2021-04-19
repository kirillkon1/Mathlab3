import sys
import matplotlib.pyplot as plt
from Functions import *
from Solvers import *


def userRead():
    integralNumber, methodNum = 0, 0

    print("Выберите интеграл:\n"
          "1) 4x^3 - 5x^2 + 6x - 7)dx x = 0..2\n"
          "2) (3^(x/3) + x/3 + 3)dx x = -3..3\n"
          "3) (ln(3x) + 3)dx x = 1..7\n"
          "4) 1/(x-2)\n"
          "5) sin(x)/x")
    while True:
        try:
            integralNumber = int(input())

            if 0 < integralNumber <= 5:
                break
            print("Неверный ввод")
        except Exception:
            print("Неверный ввод")

    a, b = find_borders(integralNumber)

    a, b, mode = changeBorder(a, b)

    print("Выберите метод решения интерграла:\n"
          "1) Метод прямоугольников\n"
          "2) Метод трапеций\n"
          "3) Метод Симпсона")

    while True:
        try:
            methodNum = int(input())
            if 0 < methodNum <= 3:
                break
            print("Неверный ввод")
        except Exception:
            print("Неверный ввод")

    func = find_func(integralNumber, a, b)

    print("Погрешность измерений. Введите кол-во знаков после запятой (Например '3' = 0.001 )")
    epsilon_int = int(input())
    while True:
        if epsilon_int < 1:
            print('А в чем смысл? Выберите другую погрешность')
            continue
        if epsilon_int > 10:
            print("Слишком большая погрешность")
            continue
        break
    return func, 0.1 ** epsilon_int, find_method(methodNum), mode


def find_borders(num: int):
    if num == 1:
        return 0, 2
    elif num == 2:
        return -3, 3
    elif num == 3:
        return 1, 7
    else:
        return 0, 0


def find_rectangle_mode():
    print("Выберите модификацию для метода прямоугольников :\n"
          "1) Правые прямоугольники\n"
          "2) Левые прямоугольники\n"
          "3) Метод средних")

    while True:
        try:
            methodNum = int(input())
            if 0 < methodNum <= 3:
                break
            print("Неверный ввод")
        except Exception:
            print("Неверный ввод")

    return methodNum


def find_method(num: int) -> AbstractMethod:
    if num == 1:
        return RectangleMethod(find_rectangle_mode())
    if num == 2:
        return TrapezoidMethod()
    if num == 3:
        return SimpsonMethod()
    else:
        return AbstractMethod()


def find_func(num: int, a: float, b: float) -> AbstractFunction:
    if num == 1:
        return TheFirstFunction(a, b)
    elif num == 2:
        return TheSecondFunction(a, b)
    elif num == 3:
        if a < 0 or b < 0:
            print("Вышел за пределы")
            sys.exit()
        return TheThirdFunction(a, b)
    elif num == 4:
        return TheFourthFunction(a, b)
    elif num == 5:
        return TheFifthFunction(a, b)
    return AbstractFunction(a, b)


def changeBorder(a, b):
    print(f"По умолчанию значения границ интеграла равны: {a, b}. Желаете ли вы их изменить? (да/нет)")
    tmp = input()
    while True:
        if tmp == 'да' or tmp == 'нет' or tmp == 'Да' or tmp == 'Нет':
            break
        print("Неверный ввод")
        tmp = input()
    if tmp == 'нет':
        return a, b, 'not'
    print("Введите два новых числа через пробел")
    while True:
        try:
            tmp = input().split()
            tmp1, tmp2 = float(tmp[0]), float(tmp[1])
            if len(tmp) == 2:
                if tmp1 > tmp2:
                    t = tmp2
                    tmp2 = tmp1
                    tmp1 = t
                break
            print("Неверный ввод")
            tmp = input().split()
        except Exception:
            print("Неверный ввод Exception")

    print(f"Новое значение границ интеграла: {tmp1, tmp2}.")

    return tmp1, tmp2, 'yes'


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

#ubbububu
def drawImage(fun: AbstractFunction):
    X = np.linspace(-4, 4, 100)
    Y = fun.find(X)

    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.plot(X, Y)

    plt.show()
