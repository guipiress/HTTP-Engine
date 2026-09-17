from url import parse_url
from connection import create_connection, create_tls
from request import send_request
from response import recv_response, separate_response, parse_headers, get_content_length


def main():
    try:
        url = input("Target: ")

        scheme, host, port, path = parse_url(url)

        print(f"Host: {host}")
        print(f"Port: {port}")

        sock = create_connection(host, port)

        if scheme == "https":
            sock = create_tls(sock, host)

        headers = {
            "Connection": "close"
        }

        send_request(sock, "GET", host, path, headers=headers)

        headers_bytes, body = recv_response(sock)

        print(headers_bytes.decode("iso-8859-1"))

        print(f"Received body: {len(body)}")


        print("----- BODY -----")
        print(body.decode("utf-8"))
        print("----- END BODY -----")
        
        sock.close()

    except (ValueError, ConnectionError, TimeoutError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
