import socket
import ssl

def create_connection(host, port):
    try:
        sock = socket.create_connection((host, port), timeout=5)
        return sock

    except socket.timeout:
        raise TimeoutError("Connection time out")
    
    except socket.gaierror:
        raise ConnectionError("Could not resolve host")
    
    except ConnectionRefusedError:
        raise ConnectionError("Connection refused")
    
    except OSError as error:
        raise ConnectionError(f"Connection error: {error}")

def create_tls(sock, host):
    context = ssl.create_default_context()
    return context.wrap_socket(sock, server_hostname=host)
