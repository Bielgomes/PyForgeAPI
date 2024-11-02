import sys
from typing import Optional

if sys.version_info < (3, 11):
    from typing_extensions import NotRequired, TypedDict
else:
    from typing import NotRequired, TypedDict


class FastipyOptions(TypedDict):
    plugin_timeout: NotRequired[Optional[float]]
