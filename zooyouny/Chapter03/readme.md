# How to run 

```
> FLASK_APP=app.py FLASK_DEBUG=1 flask run
```

# Test

```
> curl -v GET http://localhost:5000/ping
* Could not resolve host: GET
* Closing connection 0
curl: (6) Could not resolve host: GET
*   Trying 127.0.0.1:5000...
* Connected to localhost (127.0.0.1) port 5000 (#1)
> GET /ping HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.82.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: text/html; charset=utf-8
< Content-Length: 4
< Server: Werkzeug/2.0.3 Python/3.9.12
< Date: Wed, 07 Sep 2022 16:21:27 GMT
<
* Closing connection 1
pong%
```