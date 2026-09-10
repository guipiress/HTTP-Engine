def build_request(method, host, path, headers=None, body=""):
    if headers is None:
        headers = {}

    request = f"{method} {path} HTTP/1.1\r\n"
    request += f"Host: {host}\r\n"

    for name, value in headers.items():
        request += f"{name}: {value}\r\n"

    if body:
        body_bytes = body.encode("utf-8")
        request += f"Content-Length: {len(body_bytes)}\r\n"

    request += "\r\n"
    request += body

    return request
