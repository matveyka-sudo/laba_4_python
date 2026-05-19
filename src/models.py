from datetime import datetime

from src.descriptors import DescriptorId, DescriptorDescription, DescriptorPriority, DescriptorStatus, DescriptorTime
from dataclasses import dataclass


@dataclass
class Task:
    id=DescriptorId()
    description=DescriptorDescription()
    priority=DescriptorPriority()
    status=DescriptorStatus()
    time=DescriptorTime()

    @property
    def readiness_to_perform(self)->bool:
        return self._readiness_to_perform

    @readiness_to_perform.setter
    def readiness_to_perform(self,value:bool)->None:
        if not isinstance(value,bool):
            raise TypeError("readiness_to_perform must be a bool")
        self._readiness_to_perform = value

    def __init__(self,id:int,description:str,priority:int,status:bool,time:datetime,readiness_to_perform:bool):
        self.id = id
        self.description = description
        self.priority = priority
        self.status = status
        self.time = time
        self.readiness_to_perform = readiness_to_perform