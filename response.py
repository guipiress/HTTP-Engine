def recv_response(sock):
    response_bytes = b""

    while True:
        data = sock.recv(4096)

        if not data:
            break

        response_bytes += data

    return response_bytes


def separate_response(response_bytes):
    reparator = b"\r\n\r\n"

    header_end = response_bytes.find(reparator)

    if header_end == -1:
        raise ValueError("Could not find end of headers")

    headers_bytes = response_bytes[:header_end]
    body = response_bytes[header_end + 4:]

    return headers_bytes, body



