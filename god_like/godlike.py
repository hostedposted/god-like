"""
The `GodLike` classes source.
"""
import os
import sys
from typing import Callable, Optional
from flask import Flask, request
from werkzeug.serving import run_simple
from .request import Request
from .response import Response


class GodLike:
    """
    GodLike is a simple implementation of express in python.
    """
    _app: Flask

    def __init__(self, app: Optional[Flask] = None) -> None:
        self._app = app or Flask(__name__)

    def get(self, route: str) -> Callable[[Callable[[Request, Response], None]], None]:
        """
        Creates a `GET` request

        Parameters
        ----------
        route : str
            The URL rule string.

        Returns
        -------
        Callable[[Callable[[Request, Response], None]], None]
            Decorator
        """
        def inner(func: Callable[[Request, Response], None]) -> None:
            @self._app.route(route, methods=["GET"], endpoint=func.__name__)
            def _(**_) -> Response:
                response = Response()
                func(Request(request), response)
                return response.flask_response

        return inner

    def post(self, route: str) -> Callable[[Callable[[Request, Response], None]], None]:
        """
        Creates a `POST` request

        Parameters
        ----------
        route : str
            The URL rule string.

        Returns
        -------
        Callable[[Callable[[Request, Response], None]], None]
            Decorator
        """
        def inner(func: Callable[[Request, Response], None]) -> None:
            @self._app.route(route, methods=["POST"], endpoint=func.__name__)
            def _(**_) -> Response:
                response = Response()
                func(Request(request), response)
                return response.flask_response

        return inner

    def put(self, route: str) -> Callable[[Callable[[Request, Response], None]], None]:
        """
        Creates a `PUT` request

        Parameters
        ----------
        route : str
            The URL rule string.

        Returns
        -------
        Callable[[Callable[[Request, Response], None]], None]
            Decorator
        """
        def inner(func: Callable[[Request, Response], None]) -> None:
            @self._app.route(route, methods=["PUT"], endpoint=func.__name__)
            def _(**_) -> Response:
                response = Response()
                func(Request(request), response)
                return response.flask_response

        return inner

    def delete(
        self, route: str
    ) -> Callable[[Callable[[Request, Response], None]], None]:
        """
        Creates a `DELETE` request

        Parameters
        ----------
        route : str
            The URL rule string.

        Returns
        -------
        Callable[[Callable[[Request, Response], None]], None]
            Decorator
        """
        def inner(func: Callable[[Request, Response], None]) -> None:
            @self._app.route(route, methods=["DELETE"], endpoint=func.__name__)
            def _(**_) -> Response:
                response = Response()
                func(Request(request), response)
                return response.flask_response

        return inner

    def patch(
        self, route: str
    ) -> Callable[[Callable[[Request, Response], None]], None]:
        """
        Creates a `PATCH` request

        Parameters
        ----------
        route : str
            The URL rule string.

        Returns
        -------
        Callable[[Callable[[Request, Response], None]], None]
            Decorator
        """
        def inner(func: Callable[[Request, Response], None]) -> None:
            @self._app.route(route, methods=["PATCH"], endpoint=func.__name__)
            def _(**_) -> Response:
                response = Response()
                func(Request(request), response)
                return response.flask_response

        return inner

    def head(self, route: str) -> Callable[[Callable[[Request, Response], None]], None]:
        """
        Creates a `HEAD` request

        Parameters
        ----------
        route : str
            The URL rule string.

        Returns
        -------
        Callable[[Callable[[Request, Response], None]], None]
            Decorator
        """
        def inner(func: Callable[[Request, Response], None]) -> None:
            @self._app.route(route, methods=["HEAD"], endpoint=func.__name__)
            def _(**_) -> Response:
                response = Response()
                func(Request(request), response)
                return response.flask_response

        return inner

    def options(
        self, route: str
    ) -> Callable[[Callable[[Request, Response], None]], None]:
        """
        Creates a `OPTIONS` request

        Parameters
        ----------
        route : str
            The URL rule string.

        Returns
        -------
        Callable[[Callable[[Request, Response], None]], None]
            Decorator
        """
        def inner(func: Callable[[Request, Response], None]) -> None:
            @self._app.route(route, methods=["OPTIONS"], endpoint=func.__name__)
            def _(**_) -> Response:
                response = Response()
                func(Request(request), response)
                return response.flask_response

        return inner

    def listen(self, port: int = 5000, hostname: str = "localhost", verbose: bool = True) -> None:
        """
        Listens on a port for a request

        Parameters
        ----------
        port : int, optional
            The port to listen on, by default 5000
        hostname : str, optional
            The hostname to listen on, by default "localhost"
        verbose : bool, optional
            Wether the server should print on all requests, by default True
        """
        if not verbose:
            stdout = sys.stdout
            stderr = sys.stderr
            with open(os.devnull, "w") as null:
                sys.stdout = null
                sys.stderr = null

        run_simple(hostname, port, self._app, False)

        if not verbose:
            sys.stdout = stdout
            sys.stderr = stderr
