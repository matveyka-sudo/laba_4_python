import pytest
from src.models import Task
from datetime import datetime

def test_get():
    '''тесты метода гет'''
    test_task = Task(1, '1', 1, True, datetime(2026, 1, 1, 1, 1, 1), True)
    assert test_task.readiness_to_perform == True

def test_set():
    '''тесты метода set'''
    with pytest.raises(TypeError):
        Task(1,'1',1,True,datetime(2026, 1, 1, 1, 1, 1), '1')