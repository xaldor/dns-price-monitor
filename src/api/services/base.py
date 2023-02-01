from abc import ABC
from typing import Any


class ApiService(ABC):
    """Base class for sync API services."""

    async def process(self, data: Any) -> Any:
        pass


class AsyncApiService(ABC):
    """Base class for async API services."""

    async def process(self, data: Any) -> Any:
        pass
