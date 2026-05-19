from datetime import datetime
from typing import Iterable
from src.models import Task
from src.logger import logger

class Source:
    def generator(self)->Iterable[Task]:
        '''метод генерирующий задачи при помощи цикла'''
        for i in range(1,11):
            tasks=Task(id=i,description="description",priority=i,status=True,time=datetime.now(),readiness_to_perform=True)
            logger.info("задача сгенерирована")
            yield tasks