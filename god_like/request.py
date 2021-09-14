"""
A simplified version of flask's request.
"""
import mimetypes
from typing import List, Union
from flask import Request as FlaskRequest


class Request:
    """
    The `req` object represents the HTTP request that was sent to the server.

    For example:
    ```py
    @app.get("/user/<id>")
    def get_user(req, res):
        res.send(req.params["id"])
    ```

    The `req` object is an enhanced version of the `flask.Request` object. You can access the flask request object by getting the `_flask_request` attribute of the `req` object.
    """

    _flask_request: FlaskRequest

    def __init__(self, flask_request: FlaskRequest) -> None:
        self._flask_request = flask_request

    @property
    def body(self) -> str:
        """
        Contains a string with the body of the request.
        The string is empty if the request has no body.
        ```py
        import json
        from god_like import GodLike

        app = GodLike()

        @app.post("/profile/")
        def profile(req, res):
            body = json.loads(req.body)
            print(body["name"])
            res.send(body)
        ```
        """
        return self._flask_request.get_data().decode("utf-8")

    @property
    def cookies(self) -> dict:
        """
        This property contains a dictionary with the cookies that were sent with the request.
        If the request has no cookies, this property is an empty dictionary.

        ```py
        # Cookie: name=godlike
        print(req.cookies["name"])
        # => godlike
        ```
        """
        return self._flask_request.cookies

    @property
    def headers(self) -> dict:
        """
        This property contains a dictionary with the headers that were sent with the request.
        If the request has no headers, this property is an empty dictionary.

        ```py
        # Header: Accept-Language: en-US
        print(req.headers["Accept-Language"])
        # => en-US
        ```
        """
        return self._flask_request.headers

    @property
    def host(self) -> str:
        """
        Contains the hostname derived from the Host HTTP header.

        Aliased as `req.hostname`.

        ```py
        # Header: Host: example.com:3000
        print(req.host)
        # => example.com
        ```
        """
        return self._flask_request.host

    @property
    def hostname(self) -> str:
        """
        Contains the hostname derived from the Host HTTP header.

        Aliased as `req.hostname`.

        ```py
        # Header: Host: example.com:3000
        print(req.host)
        # => example.com
        ```
        """
        return self.host

    @property
    def ip(self) -> str:
        """
        Contains the remote IP address of the request.

        ```py
        print(req.ip)
        # => "127.0.0.1"
        ```
        """
        if self._flask_request.headers.getlist("X-Forwarded-For"):
            return self._flask_request.headers.getlist("X-Forwarded-For")[0]
        return self._flask_request.remote_addr

    @property
    def method(self) -> str:
        """
        Contains a string corresponding to the HTTP method of the request: `GET`, `POST`, `PUT`, and so on.
        """
        return self._flask_request.method

    @property
    def params(self) -> dict:
        """
        This property contains a dictionary with the query that were sent in the url.

        ```py
        @app.get("/user/<id>")
        def get_user(req, res):
            res.send(req.params["id"])
        ```
        """
        return self._flask_request.view_args

    @property
    def path(self) -> str:
        """
        Contains the path part of the request URL.

        ```py
        # example.com/users?sort=desc
        print(req.path)
        # => "/users"
        ```
        """
        return self._flask_request.path

    @property
    def protocol(self) -> str:
        """
        Contains the request protocol string: either http or (for TLS requests) https.

        ```py
        print(req.protocol)
        ```
        """
        return self._flask_request.scheme

    @property
    def query(self) -> dict:
        """
        This property is an object containing a property for each query string parameter in the route.
        """
        return self._flask_request.args

    @property
    def route(self) -> str:
        """
        The currently-matched route, a string. For example:

        ```py
        @app.get("/user/<id>")
        def get_user(req, res):
            print(req.route) # => "/user/<id>"
            res.send(req.route)
        ```
        """
        return self._flask_request.url_rule.endpoint

    @property
    def secure(self) -> bool:
        """
        A Boolean property that is true if a TLS connection is established. Equivalent to:

        ```py
        req.protocol == "https"
        ```
        """
        return self.protocol == "https"

    @property
    def subdomains(self) -> List[str]:
        """
        An array of subdomains in the domain name of the request.

        ```py
        # Host: "tobi.ferrets.example.com"
        print(req.subdomains)
        # => ["ferrets", "tobi"]
        ```
        """
        return list(reversed(self.hostname.split(".")))[2:]

    @property
    def url(self) -> str:
        """
        The url of the request.
        """
        return self._flask_request.url

    def accepts(self, media_type: str) -> bool:
        """
        Checks if the specified content type is acceptable, based on the request’s `Accept` HTTP header field. The method returns `True` if the content type matches, or if the specified content type is not acceptable, returns `False` (in which case, the application should respond with `406 "Not Acceptable"`).

        Parameters
        ----------
        media_type : str
            The media_type value may be a single MIME type string (such as `application/json`) or an extension name such as `json`.

        Returns
        -------
        bool
            If the specified content type is accepted.
        """
        if "/" not in media_type:
            media_type = mimetypes.types_map.get(media_type, media_type)
        return media_type in self._flask_request.accept_mimetypes

    def accepts_charset(self, charset: str) -> bool:
        """
        Returns `True` if the charset is accepted, based on the request’s `Accept-Charset` HTTP header field. If the specified charset is not accepted, returns `False`.

        Parameters
        ----------
        charset : str
            The charset

        Returns
        -------
        bool
            Returns wether the charset is accepted.
        """
        return charset in self._flask_request.accept_charsets

    def accepts_encoding(self, encoding: str) -> bool:
        """
        Returns `True` if the specified encoding is accepted, based on the request’s `Accept-Encoding` HTTP header field. If the specified encoding is not accepted, returns `False`.

        Parameters
        ----------
        encoding : str
            The encoding

        Returns
        -------
        bool
            Returns wether the encoding is accepted.
        """
        return encoding in self._flask_request.accept_encodings

    def accepts_language(self, language: str) -> bool:
        """
        Returns `True` if the specified language is accepted, based on the request’s `Accept-Language` HTTP header field. If the specified language is not accepted, returns `False`.

        Parameters
        ----------
        language : str
            The language

        Returns
        -------
        bool
            Returns wether the language is accepted.
        """
        return language in self._flask_request.accept_languages

    def get(self, header: str) -> Union[str, None]:
        """
        Returns the specified HTTP request header field (case-insensitive match).

        ```py
        req.get("Content-Type")
        # => "text/plain"

        req.get("content-type")
        # => "text/plain"

        req.get("Something")
        # => None
        ```

        Parameters
        ----------
        header : str
            The content header

        Returns
        -------
        Union[str, None]
            Returns the specified HTTP request header field (case-insensitive match).
        """
        return self._flask_request.headers.get(header)
