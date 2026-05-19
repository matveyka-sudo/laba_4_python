from typing import Any
from src.contract import Contract
from src.logger import logger



def check(lst: list[Any]) -> list[Any] | list:
    '''Функция возвращает список из задач, проверяет классы на наличие метода генерации'''
    lst2:list[Any]=[]
    for item in lst:
        if isinstance(item, Contract):
            try:
                lst1 = list(item.generator())
                lst2.append(lst1)
                logger.info("Проверка на contract пройдена")
            except Exception as e:
                logger.error(f"Непредвиденная ошибка {e}")
        else:
            logger.info("Проверка на contract не пройдена")
    res=[]
    for i in lst2:
        res+=i
    return res