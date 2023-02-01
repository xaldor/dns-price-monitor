import asyncio
from typing import Callable, TypeAlias, Coroutine, Any

FunctionNoArgumentsNoReturn: TypeAlias = Callable[[], Coroutine[Any, Any, None]]


def repeat_every(*, seconds: int):
    def decorator(func: FunctionNoArgumentsNoReturn):
        def wrapped():
            async def loop():
                while True:
                    await func()  # type: ignore
                    await asyncio.sleep(seconds)

            asyncio.ensure_future(loop())

        return wrapped

    return decorator
