import asyncio
from typing import Any, AsyncGenerator
from src.models import Task
from src.logger import logger


class TaskQueue:
    def __init__(self,tasks=None)->None:
        """метод init класса TaskQueue"""
        self._tasks = list(tasks) if tasks else []
        self._event = asyncio.Event()

        if len(self._tasks)>0:
            self._event.set()

    def push(self,task:Task | None)->None:
        """метод добавления для очереди"""
        self._tasks.append(task)
        logger.info("добавлена задача")
        self._event.set()

    async def pop(self)->Task | None:
        """метод удаления для очереди"""
        await self._event.wait()
        logger.info("задача удалена")
        task=self._tasks.pop(0)
        if len(self._tasks)==0:
            self._event.clear()
        return task

    def __len__(self)->int:
        logger.info("Длина очереди:")
        """возвращает длину очереди"""
        return len(self._tasks)

    async def filter_by_status(self)->AsyncGenerator[Task,Any]:
        """Фильтр, который проверяет статус на true, если так, то он возвращает задачу"""
        i = 0
        while i < len(self._tasks):
            if self._tasks[i].status:
                task = self._tasks.pop(i)
                yield task
            else:
                i += 1
        if len(self._tasks)==0:
            self._event.clear()



    async def filter_by_priority(self,minimum_priority:int)->AsyncGenerator[Task,Any]:
        """Фильтр, который проверяет приоритет, если он больше минимального, то возвращаем задачу"""
        i = 0
        while i < len(self._tasks):
            if self._tasks[i].priority >= minimum_priority:
                task = self._tasks.pop(i)
                yield task
            else:
                i += 1
        if len(self._tasks)==0:
            self._event.clear()

    async def filter_by_id(self,minimum_id : int)->AsyncGenerator[Task,Any]:
        """Фильтр, который проверяет id, если он больше минимального, то возвращаем задачу"""
        i = 0
        while i < len(self._tasks):
            if self._tasks[i].id >= minimum_id:
                task = self._tasks.pop(i)
                yield task
            else:
                i += 1
        if len(self._tasks)==0:
            self._event.clear()

    async def filter_by_readiness_to_perform(self)->AsyncGenerator[Task,Any]:
        """Фильтр, который проверяет готовность на true, если так, то он возвращает задачу"""
        i = 0
        while i < len(self._tasks):
            if self._tasks[i].readiness_to_perform:
                task = self._tasks.pop(i)
                yield task
            else:
                i += 1
        if len(self._tasks) == 0:
            self._event.clear()

    async def get_next_task(self)->Task | None:
        """Метод, позволяющий получить следующую задачу"""
        while len(self._tasks)==0:
            await self._event.wait()

        task = self._tasks.pop()

        if len(self._tasks)==0:
            self._event.clear()
        return task

    async def get_task_by_index(self,index:int)->Task | None:
        """Метод, который возвращает задачу по индексу"""
        try:
            await self._event.wait()
            logger.info("получена задача по индексу")
            return self._tasks[index]
        except IndexError:
            return None

    def __aiter__(self)->"TaskQueue":
        return self

    async def __anext__(self)->Task:
        """Метод для итерации по асинхронной очереди"""
        while len(self._tasks)==0:
            await self._event.wait()
        task=self._tasks.pop(0)
        if len(self._tasks)==0:
            self._event.clear()
        if task is None:
            raise StopAsyncIteration
        return task
