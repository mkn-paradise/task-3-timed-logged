import logging
import time

from timed_logged import timed_logged

logging.basicConfig(level=logging.ERROR)


@timed_logged
def slow_sum(a, b, delay=0.5):
    """Складывает два числа после заданной задержки.

    Args:
        a (int | float): Первое слагаемое.
        b (int | float): Второе слагаемое.
        delay (float): Задержка перед сложением в секундах.

    Returns:
        int | float: Сумма чисел `a` и `b`.
    """

    time.sleep(delay)
    return a + b


@timed_logged
def divide(a, b):
    """Делит одно число на другое.

    Args:
        a (int | float): Делимое.
        b (int | float): Делитель.

    Returns:
        float: Результат деления `a` на `b`.

    Raises:
        ZeroDivisionError: Возникает, если `b` равен нулю.
    """

    return a / b


slow_sum(1, 2, delay=0.2)

try:
    divide(10, 0)
except ZeroDivisionError:
    print("Ошибка поймана в основной программе")
