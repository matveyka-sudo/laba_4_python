from typing import Protocol,runtime_checkable,Iterable

@runtime_checkable
class Contract(Protocol):
    '''Класс для проверки существования метода generator'''
    def generator(self)->Iterable:
        pass