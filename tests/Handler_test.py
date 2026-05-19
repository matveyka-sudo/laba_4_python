import pytest
from datetime import datetime
from src.handlers import Handler
from src.models import Task

@pytest.fixture
def task():
    return Task(id=1, description="low", priority=1,
             status=False, time=datetime.now(), readiness_to_perform=False)
@pytest.fixture
def handler():
    return Handler()

@pytest.mark.asyncio
async def test_handler(task,handler):
    """test"""
    await handler.handle(task)
    assert task.readiness_to_perform == True