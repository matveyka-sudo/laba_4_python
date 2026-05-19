from datetime import datetime

from src.models import Task
from typing import Iterable
from src.logger import logger


class Source1:
    def __init__(self,path:str):
        self.path=path

    def generator(self)->Iterable[Task]:
        '''метод генерирующий задачи'''
        with open(self.path,"r") as f:
            for line in f.readlines():
                privet=line.split(" ")
                tasks=Task(id=int(privet[0]),description=privet[1],priority=int(privet[2]),status=bool(privet[3]),time=datetime.strptime(privet[4], "%d.%m.%Y"),readiness_to_perform=bool(privet[5]))
                logger.info("задача сгенерирована")
                yield tasks