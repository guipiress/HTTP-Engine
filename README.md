# HTTP Engine

An HTTP client built from scratch in Python to study and understand how HTTP communication works under the hood.

The project avoids high-level HTTP libraries and manually implements several parts of the communication process, including URL parsing, TCP/TLS connections, HTTP request construction, and HTTP response parsing.

> This is an educational project developed incrementally, with a focus on understanding the protocols and concepts involved rather than building a production-ready HTTP client.

---

## Objective

The main goal of HTTP Engine is not to replace libraries such as `requests` or `httpx`.

Instead, the project is designed to understand what happens between an application and a server when an HTTP request is made.

The project explores concepts such as:

- DNS and hostname resolution
- TCP
- TLS/HTTPS
- HTTP request structure
- HTTP headers
- HTTP body
- `Content-Length`
- `Transfer-Encoding: chunked`
- CRLF (`\r\n`)
- sockets
- response parsing
- cookies

---

## Technologies

- Python 3
- `socket`
- `ssl`
- Git
- GitHub

The project primarily uses Python's standard library.

---

## Project Structure

```text
HTTP Engine/
│
├── connection.py
├── cookies.py
├── main.py
├── request.py
├── response.py
├── url.py
├── .gitignore
└── README.md