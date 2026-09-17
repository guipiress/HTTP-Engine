def recv_response(sock):
    response_bytes = b""

    while b"\r\n\r\n" not in response_bytes:
        data = sock.recv(4096)

        if not data:
            break

        response_bytes += data

    headers_bytes, body = separate_response(response_bytes)

    lines = parse_headers(headers_bytes, body)

    transfer_encoding = get_transfer_encoding(lines)

    if transfer_encoding == "content-length":
        content_length = get_content_length(lines)

        while len(body) < content_length:
            data = sock.recv(4096)

            if not data:
                break

            body += data

    elif transfer_encoding == "chunked":
        remaining = body
        body = b""

        while True:
            chunk_size, remaining = receive_chunk_size(sock, remaining)

            if chunk_size == 0:
                remaining = receive_chunk_end(sock, remaining)
                break

            chunk_body, remaining = receive_chunk_body(
            sock,
            chunk_size,
            remaining
            )

            body += chunk_body

            remaining = receive_chunk_crlf(
            sock,
            remaining
            )

    else:
        raise ValueError("Could not determine response body length")

    return headers_bytes, body


def separate_response(response_bytes):
    reparator = b"\r\n\r\n"

    header_end = response_bytes.find(reparator)

    if header_end == -1:
        raise ValueError("Could not find end of headers")

    headers_bytes = response_bytes[:header_end]
    body = response_bytes[header_end + 4:]

    return headers_bytes, body


def parse_headers(headers_bytes, body):
    headers = headers_bytes.decode("iso-8859-1")

    lines = headers.split("\r\n")

    return lines


def get_content_length(lines):
    for line in lines:
        if line.lower().startswith("content-length:"):
            value = line.split(":", 1)[1].strip()
            return int(value)

    return None


def transfer_encoding_chunked(lines):
    for line in lines:
        if line.lower().startswith("transfer-encoding:"):
            value = line.split(":", 1)[1].strip()

            if value.lower() == "chunked":
                return True

    return False


def get_transfer_encoding(lines):
    content_length = get_content_length(lines)

    if content_length is not None:
        return "content-length"

    elif transfer_encoding_chunked(lines):
        return "chunked"

    else:
        return None


def receive_chunk_size(sock, remaining=b""):
    data = remaining

    while b"\r\n" not in data:
        chunk = sock.recv(4096)

        if not chunk:
            raise ConnectionError("Connection closed while reading chunk size")

        data += chunk

    line, remaining = data.split(b"\r\n", 1)

    chunk_size = int(line, 16)

    return chunk_size, remaining


def receive_chunk_body(sock, chunk_size, remaining=b""):
    body = remaining

    while len(body) < chunk_size:
        data = sock.recv(4096)

        if not data:
            raise ConnectionError("Connection closed while reading chunk body")

        body += data

    chunk_body = body[:chunk_size]
    remaining = body[chunk_size:]

    return chunk_body, remaining


def receive_chunk_crlf(sock, remaining=b""):
    data = remaining

    while len(data) < 2:
        chunk = sock.recv(4096)

        if not chunk:
            raise ConnectionError("Connection closed while reading chunk CRLF")

        data += chunk

    if data[:2] != b"\r\n":
        raise ValueError("Invalid chunk CRLF")

    return data[2:]


def receive_chunk_end(sock, remaining=b""):
    data = remaining

    while len(data) < 2:
        chunk = sock.recv(4096)

        if not chunk:
            raise ConnectionError(
                "Connection closed while reading chunk end"
            )

        data += chunk

    if data[:2] != b"\r\n":
        raise ValueError("Invalid chunk end")

    return data[2:]