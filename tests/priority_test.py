import pytest
from datetime import datetime
from src. exceptions import PriorityException
from src.models import Task

def test_get():
    '''тесты метода гет'''
    test_task=Task(1,'1',1,True,datetime(2026,1,1,1,1,1),True)
    assert test_task.priority == 1

def test_set():
    '''тесты метода set'''
    with pytest.raises(TypeError):
        test_task = Task(1, '1', '1', True, datetime(2026, 1, 1, 1, 1, 1), True)

def test_set1():
    '''тесты метода set'''
    with pytest.raises(ValueError):
        Task(1, '1', 0, True, datetime(2026, 1, 1, 1, 1, 1), True)

def test_del():
    '''тесты метода дел'''
    test_task = Task(1, '1', 1, True, datetime(2026, 1, 1, 1, 1, 1), True)
    with pytest.raises(PriorityException):
        del test_task.priority