# 1.x API

## god_like.GodLike(app = None)

Creates a GodLike application.

Takes an optional `app` argument that should be a Flask application instance, if it is not passed a Flask application will be created.

```py
from god_like import GodLike

app = GodLike()
```
