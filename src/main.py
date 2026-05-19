import asyncio
from src.generator_1 import Source
from TaskQueue import TaskQueue
from src.generator_3 import Source2
from src.executor import Executor
from src.handlers import Handler
from src.proc import check


async def main() -> None:
    '''Главная функция, точка входа в программу'''
    sources=[
        Source(),
        Source2()
    ]
    result=check(sources)
    queue=TaskQueue(result)
    queue.push(None)
    handler1=Handler()
    executor=Executor(queue,handler1)
    await executor.run()


if __name__ == "__main__":
    asyncio.run(main())
