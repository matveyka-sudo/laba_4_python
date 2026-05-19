import pytest
from datetime import datetime
from src.models import Task

def test_get():
    '''тесты метода гет'''
    test_task = Task(1, '1', 1, True, datetime(2026, 1, 1, 1, 1, 1), True)
    assert test_task.time == datetime(2026, 1, 1, 1, 1, 1)