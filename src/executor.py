from src.TaskQueue import TaskQueue
from src.protocol import Controller
from src.models import Task
from src.exceptions import AsyncOperationException
from src.logger import logger

class Executor:
    def __init__(self, queue:TaskQueue, handlers:Controller) -> None:
        self.taskQueue = queue
        self.handlers = handlers

    def execute(self,task:Task | list[Task]) -> None:
        "Метод, который добавляет задачи в очередь"
        if isinstance(task,list):
            for i in task:
                self.taskQueue.push(i)
                logger.info(f"push task {i}")
        else:
            self.taskQueue.push(task)
            logger.info(f"push task {task}")

    async def run(self):
        "Метод, который пробегается по очереди и отправляет задачи worker'у"
        async for task in self.taskQueue:
            try:
                logger.info("worker was called")
                await self.handlers.handle(task)
            except AsyncOperationException as e:
                logger.error(f"mistake : {e}")




