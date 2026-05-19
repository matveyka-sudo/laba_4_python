import pytest
from src.exceptions import StatusException
from src.models import Task
from datetime import datetime

def test_get():
    '''тесты метода гет'''
    test_task=Task(1,'1',1,True,datetime(2026,1,1,1,1,1),True)
    assert test_task.status == True

def test_set():
    '''тесты метода set'''
    with pytest.raises(TypeError):
        Task(1,'1',1,'str',datetime(2026,1,1,1,1,1),True)

def test_del():
    '''тесты метода дел'''
    test_task = Task(1, '1', 1, True, datetime(2026, 1, 1, 1, 1, 1), True)
    with pytest.raises(StatusException):
        del test_task.status