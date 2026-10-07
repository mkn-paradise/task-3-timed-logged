import logging
import time

from timed_logged import timed_logged

logging.basicConfig(level=logging.ERROR)


@timed_logged
def slow_sum(a, b, delay=0.5):
    time.sleep(delay)
    return a + b


@timed_logged
def divide(a, b):
    return a / b


slow_sum(1, 2, delay=0.2)

try:
    divide(10, 0)
except ZeroDivisionError:
    print("Ошибка поймана в основной программе")
