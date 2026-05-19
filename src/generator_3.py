from datetime import datetime
from src.models import Task
from typing import Iterable

class Source2:
    def generator(self)->Iterable[Task]:
        '''метод генерирующий задачи'''
        return [
            Task(id=1,description = 'description' , priority = 1,status = True, time = datetime.now(), readiness_to_perform=True),
            Task(id=2,description = 'description' , priority = 2,status = True, time = datetime.now(), readiness_to_perform=True),
            Task(id=3,description = 'description' , priority = 3,status = True, time = datetime.now(), readiness_to_perform=True)
        ]