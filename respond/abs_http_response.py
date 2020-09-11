from typing import Optional, Any
from http import HTTPStatus
import abc


def _create_method(code: int, *args, **kwargs):
    """ Creates a new classmethod template for an HTTP method and set its associate response code """

    def method_template(cls, *args, **kwargs):
        return cls._make_response(code, *args, **kwargs)

    return method_template


def _name_method(value):
    """ Build method name """
    return value.lower() if value != HTTPStatus.CONTINUE.name else f"{value.lower()}_"


class MetaHTTPResponse(abc.ABCMeta):
    """ Generate classmethod for each of the http methods in the standard ``http`` library """

    def __new__(cls, name, bases, attrs, **kwargs):
        _cls = super().__new__(cls, name, bases, attrs, **kwargs)

        _http_statuses = {_name_method(r.name): r.value for r in HTTPStatus}
        for name, code in _http_statuses.items():
            attrs[name] = setattr(_cls, name, classmethod(_create_method(code)))

        return _cls


class HTTPResponse(metaclass=MetaHTTPResponse):
    """ HTTPResponse abstract base class """

    @classmethod
    @abc.abstractmethod
    def _make_response(cls, status: int, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        raise NotImplementedError
