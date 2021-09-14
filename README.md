# GodLike

Normally when I work on a web server I use express with JavaScript instead of flask with Python.
Even though I like python, I don't like flask.
Express is a great tool for web development, it's in JavaScript though.
So I decided to write a version of express in Python.

I came up with the name "god-like" because of how god like it would be to use express in Python.

Lets see how it works.

```py
from god_like import GodLike

app = GodLike()

@app.post("/")
def index(req, res):
    res.send(f"The body is {req.body}")

app.listen(port=8080)
```

Flask equivalent:

```py
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods["POST"])
def index():
    return f"The body is {request.data.decode('utf-8')}"

app.run(port=8080)
```

Documentation: https://hostedposted.github.io/god-like/
