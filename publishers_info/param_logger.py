import os
import datetime
import logging
from functools import wraps




def logger(path):

    def __logger(old_function):

        @wraps(old_function)
        def new_function(*args, **kwargs):
            loger = logging.getLogger(path)
            if loger.hasHandlers() == False:
                loger.setLevel(logging.DEBUG)
                FH = logging.FileHandler(path, encoding='utf-8')
                loger.addHandler(FH)

            func_call_time = datetime.datetime.now()
            result = old_function(*args, **kwargs)

            loger.info(f'Дата и время вызова функции: {func_call_time}.')
            loger.info(f'Название функции: {old_function.__name__}.')
            loger.info(f'Позиционные аргументы: {args}, именованные: {kwargs}.')
            loger.info(f'Возвращаемое значение: {result}.')
            loger.info('')

            return result

        return new_function

    return __logger
