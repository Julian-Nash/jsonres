# respond

![Python package](https://github.com/Julian-Nash/respond/workflows/Python%20package/badge.svg?branch=master)

`respond` is a small, lightweight wrapper around Flask's `make_response` and `jsonify`, providing a fast and convenient
way to return JSON, XML or plaintext data with the right HTTP status code and headers.

`respond` utilizes the RFC HTTP status code descriptions as methods, you simply call a static method
such as `ok`, `not_found` or `internal_server_error` against the data type you with to return, optionally passing in
 a dictionary of headers to set on the response.

__Python v3.6 + (100% coverage)__

```shell script
Name                           Stmts   Miss  Cover   Missing
------------------------------------------------------------
respond/__init__.py                4      0   100%
respond/abs_http_response.py     188      0   100%
respond/json_response.py          11      0   100%
respond/responder.py               7      0   100%
respond/text_response.py          12      0   100%
respond/xml_response.py           12      0   100%
------------------------------------------------------------
TOTAL                            234      0   100%

```

## Installation

```shell script
pip install respond
```

## Usage

Import the `Responder` class

```py3
from respond import Responder
```

You can now call one of many staticmethods of the class

Return a `200 OK` status code and a list

```py3
@app.route("/")
def example():
    """ Returns a list with an HTTP 200 OK status code """
    return Responder.json.ok([1, 2, 3])
```

Return a `400 BAD REQUEST` status code and a dict

```py3
@app.route("/")
def example():
    """ Returns a dict with an HTTP 400 BAD REQUEST status code """
    return Responder.json.bad_request({"error": {"message": "You did something wrong"}})
```

Return a `500 INTERNAL SERVER ERROR` status code

```py3
@app.route("/")
def example():
    """ Returns a dict with an HTTP 500 INTERNAL SERVER ERROR status code """
    return Responder.json.internal_server_error({"error": {"message": "We did something wrong"}})
```

Passing no data to the method returns an empty string

```py3
@app.route("/")
def ok():
    """ Return an empty HTTP 204 NO CONTENT response """
    return Responder.json.no_content()
```

You can optionally pass in a headers dict if required

```py3
@app.route("/")
def example():
    """ Return a dict with custom headers """
    return Responder.json.ok(data={"message": "ok"}, headers={"X-Custom-Header": "hello!"})
```

On inspecting the response, we can see our custom header:

```shell script
Content-Length: 17
Date: Sun, 03 May 2020 16:49:41 GMT
Content-Type: application/json
Server: Werkzeug/1.0.1 Python/3.8.2
X-Custom-Header: hello!
```

The `Responder` class has methods for all HTTP status codes defined by the ietf - https://tools.ietf.org/html/rfc7231

Common status codes include, `404 NOT FOUND`, here being used in a Flask error handler

```py3
def handle_not_found_error(e):
    """ Handler for not found errors """
    app.logger.warning(e)
    return Responder.json.not_found(data={"message": "Not found"})

app.register_error_handler(404, handle_not_found_error)
```

And `500 INTERNAL SERVER ERROR`

```py3
@app.route("/internal-server-error")
def internal_server_error():
    data: dict = {"error": {"message": "Whoops, we did something wrong"}}
    return Responder.json.internal_server_error(data)
```

Visiting this URL in the browser returns

```shell script
{"error": {"message": "Whoops, we did something wrong"}
```

You may also import individual classes for the specific data types JSON, XML and text using `JSONResponse`, 
`XMLResponse` and `TextResponse` respectively.

```py3
from respond import JSONResponse

@app.route("/internal-server-error")
def internal_server_error():
    data: dict = {"error": {"message": "Whoops, we did something wrong"}}
    return JSONResponse.internal_server_error(data)
```

## Extending

The `HTTPResponse` abstract base class provides an interface for all of the HTTP status codes and defines a single
 abstract method called `_make_response`.
 
Users can implement their own class by inheriting from `HTTPResponse` and implementing the `_make_response` method
, accepting 4 parameters `status`, `data`, `headers` and `**kwargs`.

```py3
class HTTPResponse(abc.ABC):
    """ HTTPResponse abstract base class """

    @classmethod
    @abc.abstractmethod
    def _make_response(cls, status: int, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        raise NotImplementedError
```

## Methods available

**100 range (informational)**

| method | HTTP Status code |
| ------ | ---------------- |
| `continue` | `100 `|
| `switching_protocol` | `101 `|
| `processing` | `102 `|
| `early_hints` | `103 `|

**200 range (success)**

| method | HTTP Status code |
| ------ | ---------------- |
| `ok` | `200 `|
| `created` | `201 `|
| `accepted` | `202 `|
| `non_authoritative_information` | `203 `|
| `no_content` | `204 `|
| `reset_content` | `205 `|
| `partial_content` | `206 `|
| `multi_status` | `207 `|
| `already_reported` | `208 `|
| `im_used` | `226 `|

**300 range (redirection)**

| method | HTTP Status code |
| ------ | ---------------- |
| `multiple_choice` | `300 `|
| `moved_permanently` | `301 `|
| `found` | `302 `|
| `see_other` | `303 `|
| `not_modified` | `304 `|
| `use_proxy` | `305 `|
| `unused` | `306 `|
| `temporary_redirect` | `307 `|
| `permanent_redirect` | `308 `|

**400 range (client error)**

| method | HTTP Status code |
| ------ | ---------------- |
| `bad_request` | `400 `|
| `unauthorized` | `401 `|
| `payment_required` | `402 `|
| `forbidden` | `403 `|
| `not_found` | `404 `|
| `method_not_allowed` | `405 `|
| `not_acceptable` | `406 `|
| `proxy_authentication_required` | `407 `|
| `request_timeout` | `408 `|
| `conflict` | `409 `|
| `gone` | `410 `|
| `length_required` | `411 `|
| `precondition_failed` | `412 `|
| `payload_too_large` | `413 `|
| `uri_too_long` | `414 `|
| `unsupported_media_type` | `415 `|
| `requested_range_not_satisfiable` | `416 `|
| `expectation_failed` | `417 `|
| `misdirected_request` | `421 `|
| `unprocessable_entity` | `422 `|
| `locked` | `423 `|
| `failed_dependency` | `424 `|
| `too_early` | `425 `|
| `upgrade_required` | `426 `|
| `precondition_required` | `428 `|
| `too_many_requests` | `429 `|
| `request_header_fields_too_large` | `431 `|
| `unavailable_for_legal_reasons` | `451 `|

**500 range (server error)**

| method | HTTP Status code |
| ------ | ---------------- |
| `internal_server_error` | `500 `|
| `not_implemented` | `501 `|
| `bad_gateway` | `502 `|
| `service_unavailable` | `503 `|
| `gateway_timeout` | `504 `|
| `http_version_not_supported` | `505 `|
| `variant_also_negotiates` | `506 `|
| `insufficient_storage` | `507 `|
| `loop_detected` | `508 `|
| `not_extended` | `510 `|
| `network_authentication_required` | `511 `|
