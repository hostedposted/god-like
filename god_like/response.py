"""
A simplified version of flask's response.
"""
from __future__ import annotations
import http
import json
import mimetypes
from pathlib import Path
from typing import Optional, Union
from flask import Response as FlaskResponse


class Response:
    """
    The `res` object represents the HTTP response that a GodLike app sends when it gets an HTTP request.

    For example:

    ```py
    @app.get("/user/<id>")
    def get_user(req, res):
        res.send(req.params["id"])
    ```

    The `res` object is an enhanced version of `flask.Response` object. You can access the flask response object by getting the `flask_response` attribute of the `res` object.
    """

    flask_response: FlaskResponse

    def __init__(self) -> None:
        self.flask_response = FlaskResponse()

    def content_type(self, content_type: str) -> Response:
        """
        Sets the `Content-Type` HTTP header to the MIME type as determined by the specified type. If type contains the `/` character, then it sets the `Content-Type` to the exact value of `type`, otherwise it is assumed to be a file extension and the MIME type is looked up in a mapping using the `mimetypes.types_map.get` method.

        Parameters
        ----------
        content_type : str
            The content type to set.

        Returns
        -------
        Response
            Returns self.
        """
        if "/" not in content_type:
            content_type = mimetypes.types_map.get("." + content_type, "text/html")
        self.flask_response.content_type = content_type
        return self

    def download(
        self, path: Union[str, Path], filename: Optional[str] = None
    ) -> Response:
        """
        Transfers the file at path as an "attachment". Typically, browsers will prompt the user for download. By default, the Content-Disposition header "filename=" parameter is path (this typically appears in the browser dialog). Override this default with the filename parameter.

        Parameters
        ----------
        path : Union[str, Path]
            The path to the file to be downloaded.
        filename : Optional[str], optional
            The name the file should be downloaded as, by default None

        Returns
        -------
        Response
            Returns self.
        """
        if isinstance(path, str):
            path = Path(path)
        self.set_header(
            {"Content-Disposition": f"attachment; filename={filename or path.name}"}
        )
        self.send_file(path)
        return self

    def get(self, field: str) -> Union[str, None]:
        """
        Returns the HTTP response header specified by `field`. The match is case-insensitive.

        Parameters
        ----------
        field : str
            The header to get

        Returns
        -------
        Union[str, None]
            Returns the HTTP response header specified by `field`.
        """
        return self.flask_response.headers.get(field, None)

    def json(self, obj: Union[dict, list, tuple, int, float, bool]) -> Response:
        """
        Sends a JSON response. This method sends a response (with the correct content-type) that is the parameter converted to a JSON string using [json.dumps](https://docs.python.org/3/library/json.html#json.dumps).

        Parameters
        ----------
        obj : Union[dict, list, tuple, int, float, bool]
            The object to be converted to a JSON string.

        Returns
        -------
        Response
            Returns self.
        """
        self.flask_response.content_type = "application/json"
        self.flask_response.data = json.dumps(obj)
        return self

    def redirect(self, path: str) -> Response:
        """
        Redirects to the URL derived from the specified path.

        Parameters
        ----------
        path : str
            The URL to redirect to.

        Returns
        -------
        Response
            Returns self.
        """
        self.flask_response.status_code = 302
        self.flask_response.data = f"""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to target URL: <a href="{path}">{path}</a>.  If not click the link.
"""
        self.content_type("text/html")
        self.flask_response.headers["Location"] = path
        return self

    def send(self, body: Union[str, dict, list, tuple, int, float, bool]) -> Response:
        """
        Sends the HTTP response.

        Parameters
        ----------
        body : Union[str, dict, list, tuple, int, float, bool]
            The body parameter can be a string, list, dict, tuple, int, float, bool. For example:

        Returns
        -------
        Response
            Returns self.
        """
        if not isinstance(body, str):
            return self.json(body)
        self.flask_response.data = body
        if self.get("Content-Type") == None:
            self.content_type("text/html")
        return self

    def send_file(self, file_path: Union[str, Path]) -> Response:
        """
        Transfers the file at the given path. Sets the Content-Type response HTTP header field based on the filename's extension.

        Parameters
        ----------
        file_path : Union[str, Path]
            The file to be sent.

        Returns
        -------
        Response
            Returns self.
        """
        if isinstance(file_path, str):
            file_path = Path(file_path)
        self.flask_response.data = file_path.read_text()
        self.flask_response.content_type = mimetypes.types_map.get(
            file_path.suffix, "text/html"
        )
        return self

    def send_status(self, code: int) -> Response:
        """
        Sets the response HTTP status code to `code` and sends the registered status message as the text response body. If an unknown status code is specified, the response body will just be the code number.

        Parameters
        ----------
        code : int
            The status code to send.

        Returns
        -------
        Response
            Returns self.
        """
        self.status(code).send(http.HTTPStatus(code).phrase or str(code))
        return self

    def set_header(self, fields: dict) -> Response:
        """
        Sets the response's HTTP headers field to value.

        Parameters
        ----------
        fields : dict
            Headers to set.

        Returns
        -------
        Response
            Returns self.
        """
        for field, value in fields.items():
            self.flask_response.headers[field] = value
        return self

    def status(self, code: int) -> Response:
        """
        Sets the HTTP status for the response.

        Parameters
        ----------
        code : int
            The status code to set the response to.

        Returns
        -------
        Response
            Returns self.
        """
        self.flask_response.status_code = code
        return self
