import logging
import time
from functools import wraps


def timed_logged(function):
    """Измеряет время выполнения функции и записывает результат или ошибку.

    Args:
        function (Callable): Функция, которую нужно обернуть декоратором.

    Returns:
        Callable: Обёрнутая функция с измерением времени выполнения.
    """

    @wraps(function)
    def wrapper(*arguments, **named_arguments):
        start_time = time.perf_counter()
        error = None

        try:
            result = function(*arguments, **named_arguments)
        except Exception as caught_error:
            error = caught_error
        finally:
            elapsed_time = (time.perf_counter() - start_time) * 1000

        if error is not None:
            logging.error(
                f"Ошибка в функции {function.__name__}: "
                f"{type(error).__name__}: {error}. "
                f"Время выполнения: {elapsed_time:.2f} мс",
                exc_info=(type(error), error, error.__traceback__),
            )
            raise error

        print(
            f"Функция: {function.__name__}; "
            f"Аргументы: args={arguments}, "
            f"named_args={named_arguments}; "
            f"Результат: {result}; "
            f"Время: {elapsed_time:.2f} мс"
        )

        return result

    return wrapper
