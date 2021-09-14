# Response

The `res` object represents the HTTP response that a GodLike app sends when it gets an HTTP request.

For example:

```py
@app.get("/user/<id>")
def get_user(req, res):
    res.send(req.params["id"])
```

The `res` object is an enhanced version of `flask.Response` object. You can access the flask response object by getting the `flask_response` attribute of the `res` object.

## Properties

### res.flask_response

The `flask.Response` object that the `res` object wraps.

## Methods

### res.content_type(content_type)

Sets the `Content-Type` HTTP header to the MIME type as determined by the specified type. If type contains the `/` character, then it sets the `Content-Type` to the exact value of `type`, otherwise it is assumed to be a file extension and the MIME type is looked up in a mapping using the `mimetypes.types_map.get` method.

```py
res.content_type(".html")
res.content_type("html")
res.content_type("json")
res.content_type("application/json")
res.content_type("png")
```

### res.download(path, filename = None)

Transfers the file at path as an "attachment". Typically, browsers will prompt the user for download. By default, the Content-Disposition header "filename=" parameter is path (this typically appears in the browser dialog). Override this default with the filename parameter.

This method uses res.send_file() to transfer the file.

```py
res.download("file.pdf")

res.download("random_file.pdf", filename="file.pdf")
```

### res.get(field)

Returns the HTTP response header specified by `field`. The match is case-insensitive.

```py
res.get("Content-Type")
```

### res.json(obj)

Sends a JSON response. This method sends a response (with the correct content-type) that is the parameter converted to a JSON string using [json.dumps](https://docs.python.org/3/library/json.html#json.dumps).

The parameter can be any JSON type, including dictionary, list, string, boolean, int or float, and you can also use it to convert other values to JSON.

```py
res.json(None)
res.json({"user": "tobi"})
res.status(500).json({ "error": "message" })
```

### res.redirect(path)

Redirects to the URL derived from the specified path.

```py
res.redirect("/foo/bar")
res.redirect("http://example.com")
res.redirect("../login")
```

### res.send(body)

Sends the HTTP response.

The body parameter can be a string, list, dict, tuple, int, float, bool. For example:

```py
res.send({ "some": "json" })
res.send("<p>some html</p>")
res.status(404).send("Sorry, we cannot find that!")
res.status(500).send({ "error": "something blew up" })
```

### res.send_file(file_path)

Transfers the file at the given path. Sets the Content-Type response HTTP header field based on the filename's extension.

```py
res.send_file("file.pdf")
```

### res.send_status(code)

Sets the response HTTP status code to `code` and sends the registered status message as the text response body. If an unknown status code is specified, the response body will just be the code number.

```py
res.sendStatus(404)
```

### res.set_header(fields)

Sets the response's HTTP headers field to value.

```py
res.set_header({
    "Content-Type": "text/plain",
    "Content-Length": "123",
    "ETag": "12345"
})
```

### res.status(code)

Sets the HTTP status for the response.

```py
res.status(400).send("Bad Request")
res.status(404).send_file("/absolute/path/to/404.png")
```
