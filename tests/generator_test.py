import pytest
from src.generator_1 import Source


def test_generate():
    '''тесты генератора'''
    generator = Source()
    for task in generator.generator():
        assert task.description == 'description'