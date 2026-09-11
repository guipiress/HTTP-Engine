def recv_response(sock):
    response_bytes = b""

    while True:
        data = sock.recv(4096)

        if not data:
            break

        response_bytes += data

    return response_bytes



