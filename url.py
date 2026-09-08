from urllib.parse import urlsplit


def parse_url(url):
    parsed = urlsplit(url)

    if parsed.scheme not in ("http", "https"):
        raise ValueError("Scheme must be HTTP or HTTPS")

    if not parsed.hostname:
        raise ValueError("Invalid URL")

    scheme = parsed.scheme
    host = parsed.hostname

    if parsed.port:
        port = parsed.port
    elif scheme == "https":
        port = 443
    else:
        port = 80

    path = parsed.path or "/"

    if parsed.query:
        path += "?" + parsed.query

    return scheme, host, port, path
