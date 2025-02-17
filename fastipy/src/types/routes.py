import sys
from typing import Callable, Coroutine, Union

if sys.version_info < (3, 11):
    from typing_extensions import Callable, List, NotRequired, TypedDict
else:
    from typing import Callable, List, NotRequired, TypedDict

FunctionType = Union[Callable, Coroutine]


class RouteHookType(TypedDict):
    onRequest: NotRequired[List[FunctionType]]
    preHandler: NotRequired[List[FunctionType]]
    onResponse: NotRequired[List[FunctionType]]
    onError: NotRequired[List[FunctionType]]


class PrintTreeOptionsType(TypedDict):
    include_hooks: NotRequired[bool]
    include_middlewares: NotRequired[bool]


RouteMiddlewareType = List[FunctionType]
