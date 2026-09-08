from url import parse_url
from connection import create_connection, create_tls
from request import build_request


def main():
    try:
        url = input("Target: ")
        scheme, host, port, path = parse_url(url)

        print(f"Host: {host}")
        print(f"Port: {port}")

        sock = create_connection(host, port)
        if scheme == "https":
            sock = create_tls(sock, host)

        print("Connection successful!")

        sock.close()

    except (ValueError, ConnectionError, TimeoutError) as error:
        print(f"Error: {error}")

def main():
    request = build_request(
        "GET",
        "example.com",
        "/"
    )
    print(request)


if __name__ == "__main__":
    main()
