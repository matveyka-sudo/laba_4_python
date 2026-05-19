import pytest
from datetime import datetime
from src.models import Task
from src.TaskQueue import TaskQueue

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
def queue(valid_tasks):
    """Инициализирует очередь перед каждым тестом"""
    return TaskQueue(valid_tasks)

def test_push(queue):
    queue.push(Task(id=4, description="low", priority=1,status=True,time=datetime.now(), readiness_to_perform=False))
    assert queue._tasks[3].id == 4

@pytest.mark.asyncio
async def test_pop_task(queue):
    task = await queue.pop()
    assert task.id == 1
    task1 = await queue.pop()
    assert task1.id == 2
    task2 = await queue.pop()
    assert task2.id == 3

def test_len(queue):
    assert queue.__len__() == 3

@pytest.mark.asyncio
async def test_filter_by_status(queue):
    tasks = [task async for task in queue.filter_by_status()]

    assert len(tasks) > 0
    assert tasks[0].id == 2

@pytest.mark.asyncio
async def test_filter_by_priority(queue):
    tasks = [task async for task in queue.filter_by_priority(6)]
    assert len(tasks)>0
    assert tasks[0].id == 2

@pytest.mark.asyncio
async def test_filter_by_id(queue):
    tasks = [task async for task in queue.filter_by_id(3)]
    assert len(tasks)>0
    assert tasks[0].id == 3

@pytest.mark.asyncio
async def test_filter_by_readiness_to_perform(queue):
    tasks = [task async for task in queue.filter_by_readiness_to_perform()]
    assert len(tasks)>0
    assert tasks[0].id == 3


@pytest.mark.asyncio
async def test_get_next_task(queue):
    task = await queue.get_next_task()
    assert task.id == 3

@pytest.mark.asyncio
async def test_get_task_by_index(queue):
    task = await queue.get_task_by_index(0)
    assert task.id == 1

