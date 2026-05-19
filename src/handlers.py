import asyncio
from src.models import Task
from src.logger import logger

class Handler:
    async def handle(self,task: Task):
        """worker"""
        logger.info("worker accepted the task")
        await asyncio.sleep(1)
        task.readiness_to_perform = True
