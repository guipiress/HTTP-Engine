from url import parse_url
from connection import create_connection

def main():
    url = input("Target: ")

    scheme, host, port, path = parse_url(url)

    print(f'Host: {host}')
    print(f'Port: {port}')

    sock = create_connection(host, port)

    print("Connection successful!")

    sock.close()

if __name__ == "__main__":
    main()
