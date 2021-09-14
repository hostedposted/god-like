# Request

The `req` object represents the HTTP request that was sent to the server.

For example:
```py
@app.get("/user/<id>")
def get_user(req, res):
    res.send(req.params["id"])
```

The `req` object is an enhanced version of the `flask.Request` object. You can access the flask request object by getting the `_flask_request` attribute of the `req` object.

## Properties

### req.body

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

### req.cookies

This property contains a dictionary with the cookies that were sent with the request.
If the request has no cookies, this property is an empty dictionary.

```py
# Cookie: name=godlike
print(req.cookies["name"])
# => godlike
```

### req.headers

This property contains a dictionary with the headers that were sent with the request.
If the request has no headers, this property is an empty dictionary.

```py
# Header: Accept-Language: en-US
print(req.headers["Accept-Language"])
# => en-US
```

### req.host

Contains the hostname derived from the Host HTTP header.

Aliased as `req.hostname`.

```py
# Header: Host: example.com:3000
print(req.host)
# => example.com
```

### req.ip

Contains the remote IP address of the request.

```py
print(req.ip)
# => "127.0.0.1"
```

### req.method

Contains a string corresponding to the HTTP method of the request: `GET`, `POST`, `PUT`, and so on.

### req.params

This property contains a dictionary with the query that were sent in the url.

```py
@app.get("/user/<id>")
def get_user(req, res):
    res.send(req.params["id"])
```

### req.path

Contains the path part of the request URL.

```py
# example.com/users?sort=desc
print(req.path)
# => "/users"
```

### req.protocol

Contains the request protocol string: either http or (for TLS requests) https.

```py
print(req.protocol)
```

### req.query

This property is an object containing a property for each query string parameter in the route.

### req.route

The currently-matched route, a string. For example:

```py
@app.get("/user/<id>")
def get_user(req, res):
    print(req.route) # => "/user/<id>"
    res.send(req.route)
```

### req.secure

A Boolean property that is true if a TLS connection is established. Equivalent to:

```py
req.protocol == "https"
```

### req.subdomains

An array of subdomains in the domain name of the request.

```py
# Host: "tobi.ferrets.example.com"
print(req.subdomains)
# => ["ferrets", "tobi"]
```

### req.url

The url of the request.

## Methods

### req.accepts(media_type)

Checks if the specified content type is acceptable, based on the request’s `Accept` HTTP header field. The method returns `True` if the content type matches, or if the specified content type is not acceptable, returns `False` (in which case, the application should respond with `406 "Not Acceptable"`).

The media_type value may be a single MIME type string (such as `application/json`) or an extension name such as `json`.

```py
# Accept: text/html
req.accepts("html")
# => True

# Accept: text/*, application/json
req.accepts("html")
# => True
req.accepts("text/html")
# => True
req.accepts("application/json")
# => True

# Accept: text/*, application/json
req.accepts("image/png")
req.accepts("png")
# => False
```

### req.accepts_charset(charset)

Returns `True` if the charset is accepted, based on the request’s `Accept-Charset` HTTP header field. If the specified charset is not accepted, returns `False`.

### req.accepts_encoding(encoding)

Returns `True` if the specified encoding is accepted, based on the request’s `Accept-Encoding` HTTP header field. If the specified encoding is not accepted, returns `False`.

### req.accepts_language(language)

Returns `True` if the specified language is accepted, based on the request’s `Accept-Language` HTTP header field. If the specified language is not accepted, returns `False`.

### req.get(field)

Returns the specified HTTP request header field (case-insensitive match).

```py
req.get("Content-Type")
# => "text/plain"

req.get("content-type")
# => "text/plain"

req.get("Something")
# => None
```