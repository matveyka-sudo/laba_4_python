from typing import Protocol
from src.models import Task


class Controller(Protocol):
    async def handle(self,task:Task):
        pass