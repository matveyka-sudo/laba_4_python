

from src.exceptions import IdException, DescriptionException, PriorityException, StatusException, TimeException
from datetime import datetime
from src.logger import logger

class DescriptorId:
    def __set_name__(self,owner,name:str)->None:
        self.name = name
        self.private_name = '_'+name


    def __get__(self,instance,owner)->int:
        '''получаем значение айди'''
        logger.info("get id")
        if instance is None:
            logger.error("Id can only be obtained from an existing task")
            raise IdException("ID can only be obtained from an existing task")
        return getattr(instance,self.private_name,None)

    def __set__(self, instance, value : int)->None:
        '''ставим значение айди'''
        logger.info("set id")
        if not isinstance(value,int):
            logger.error("Id must be an integer")
            raise TypeError("Id must be an integer")
        if value < 0:
            logger.error("Id must be positive")
            raise ValueError("Id must be positive")
        if hasattr(instance,self.private_name):
            logger.error("Id can only be obtained from an existing task")
            raise IdException("Id already set")
        if instance is None:
            logger.error("Id can only be obtained from an existing task")
            raise IdException("Id can be only in real task")
        setattr(instance,self.private_name,value)

    def __delete__(self,instance)->None:
        '''делитер для айди'''
        logger.info("delete id")
        raise IdException("You can't delete task IDs")

class DescriptorDescription:
    def __set_name__(self,owner,name:str)->None:
        self.name = name
        self.private_name = '_'+name

    def __get__(self, instance, owner)->str:
        '''получаем описание'''
        logger.info("get description")
        if instance is None:
            logger.error("Description can only be obtained from an existing task")
            raise DescriptionException("Description can only be obtained from an existing task")
        return getattr(instance,self.private_name,None)

    def __set__(self,instance,value:str)->None:
        '''устанавливаем описание'''
        logger.info("set description")
        if not isinstance(value,str):
            logger.error("Description must be a string")
            raise TypeError("Description must be a string")
        if len(value)==0:
            logger.error("Description cannot be empty")
            raise ValueError("Description must be a non-empty string")
        if instance is None:
            logger.error("Description can be obtained from an existing task")
            raise DescriptionException("Description can be only in real task")
        setattr(instance,self.private_name,value)

    def __delete__(self,instance)->None:
        '''делитер для описания'''
        logger.info("delete description")
        raise DescriptionException("You can't delete task description")

class DescriptorPriority:
    def __set_name__(self,owner,name:str)->None:
        self.name = name
        self.private_name = '_'+name

    def __get__(self, instance, owner)->int:
        '''получаем приоритет'''
        logger.info("get priority")
        if instance is None:
            logger.error("Priority can only be obtained from an existing task")
            raise PriorityException("Priority can only be obtained from an existing task")
        return getattr(instance,self.private_name,None)

    def __set__(self,instance,value:int)->None:
        '''устанавливаем приоритет'''
        logger.info("set priority")
        if not isinstance(value,int):
            logger.error("Priority must be an integer")
            raise TypeError("Priority must be an non-empty integer")
        if value<=0:
            logger.error("Priority must be positive")
            raise ValueError("Priority must be positive")
        if instance is None:
            logger.error("Priority can be obtained from an existing task")
            raise PriorityException("Priority can be only in real task")
        setattr(instance,self.private_name,value)

    def __delete__(self,instance)->None:
        '''делитер для приоритета'''
        logger.info("delete priority")
        raise PriorityException("You can't delete priority")

class DescriptorStatus:
    def __set_name__(self,owner,name:str)->None:
        self.name = name
        self.private_name = '_'+name

    def __get__(self, instance, owner)->bool:
        '''получаем статус'''
        logger.info("get status")
        if instance is None:
            logger.error("Status can only be obtained from an existing task")
            raise StatusException("Status can only be obtained from an existing task")
        return getattr(instance,self.private_name,None)

    def __set__(self,instance,value:bool)->None:
        '''устанавливаем статус'''
        logger.info("set status")
        if not isinstance(value,bool):
            logger.error("Status must be a boolean")
            raise TypeError("Status must be a boolean")
        if instance is None:
            logger.error("Status can be obtained from an existing task")
            raise StatusException("Status can be only in real task")
        setattr(instance,self.private_name,value)

    def __delete__(self,instance)->None:
        '''делитер для статуса'''
        logger.info("delete status")
        raise StatusException("You can't delete status")

class DescriptorTime:
    def __set_name__(self,owner,name:str)->None:
        self.name = name
        self.private_name = '_'+name

    def __get__(self,instance,owner)->datetime:
        '''получаем время'''
        logger.info("get time")
        if instance is None:
            logger.error("Time can only be obtained from an existing task")
            raise TimeException("Time can only be obtained from an existing task")
        return getattr(instance,self.private_name,None)