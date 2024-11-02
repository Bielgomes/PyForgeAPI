__version__ = "1.5.3"

from starlette.testclient import TestClient

from .src.classes.json_database import Database
from .src.classes.mailer import Mailer, create_message
from .src.classes.template_render import render_template
from .src.constants.http_status_code import Status
from .src.core.fastipy import Fastipy, FastipyInstance
from .src.core.reply import Reply
from .src.core.request import Request
from .src.exceptions.exception_handler import ExceptionHandler
from .src.types.plugins import PluginOptions

__all__ = [
    "Fastipy",
    "FastipyInstance",
    "PluginOptions",
    "Request",
    "Reply",
    "Mailer",
    "create_message",
    "render_template",
    "Database",
    "Status",
    "ExceptionHandler",
    "TestClient",
]
