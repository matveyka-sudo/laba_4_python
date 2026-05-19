import pytest
from datetime import datetime
from src.TaskQueue import TaskQueue
from src.executor import Executor
from src.handlers import Handler
from src.models import Task

@pytest.fixture
def valid_tasks():
    """Создает набор задач для тестирования очереди"""
    return [
        Task(id=1, description="low", priority=1,
             status=False, time=datetime.now(), readiness_to_perform=False),
        Task(id=2, description="high", priority=10,
             status=True, time=datetime.now(), readiness_to_perform=False),
        Task(id=3, description="medium", priority=5,
             status=False, time=datetime.now(), readiness_to_perform=True),
    ]

@pytest.fixture
def handler():
    return Handler()


@pytest.mark.asyncio
async def test_executor(valid_tasks,handler):
    empty_queue = TaskQueue()
    executor = Executor(empty_queue, handler)
    executor.execute(valid_tasks)

    first_task = await empty_queue.pop()
    assert first_task.id == 1




