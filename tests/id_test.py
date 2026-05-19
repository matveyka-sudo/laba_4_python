import pytest
from datetime import datetime
from src.exceptions import IdException
from src.models import Task

def test_get():
    '''тесты метода гет'''
    test_task=Task(1,'1',1,True,datetime(1,1,1,1,1,1),True)
    assert test_task.id == 1

def test_set():
    '''тесты метода set'''
    test_task=Task(1,'1',1,True,datetime(1,1,1,1,1,1),True)
    with pytest.raises(IdException):
        test_task.id=2

def test_set1():
    '''тесты метода set'''
    with pytest.raises(TypeError):
        test_task=Task('1','1',1,True,datetime(1,1,1,1,1,1),True)

def test_set2():
    '''тесты метода set'''
    with pytest.raises(ValueError):
        test_task=Task(-1,'1',1,True,datetime(1,1,1,1,1,1),True)

def test_del():
    '''тесты метода дел'''
    test_task=Task(1,'1',1,True,datetime(1,1,1,1,1,1),True)
    with pytest.raises(IdException):
        del test_task.id