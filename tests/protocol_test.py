import pytest
from typing import runtime_checkable, Protocol
from src.models import Task
from src.handlers import Handler


@pytest.fixture
def controller():
    return Handler()

@runtime_checkable
class Controller(Protocol):
    def handle(self,task:Task):
        pass

def test_controller(controller):
    assert isinstance(controller,Controller) is True

