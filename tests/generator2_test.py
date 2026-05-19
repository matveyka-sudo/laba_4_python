import pytest
from src.generator_2 import Source1


@pytest.fixture()
def source1():
    return Source1("tests/12.txt")

def test_source1(source1):
    tasks = list(source1.generator())
    assert len(tasks) == 4