import socket
import sys
import json

with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
    s.connect("./debug.sock")

    message = {
        "seq": 1,
        "type": "request",
        "command": "initialize"
    }

    message_bytes = json.dumps(message).encode("utf-8")
    header_bytes = f"Content-Length: {len(message_bytes)}\r\n\r\n".encode("utf-8")
    s.sendall(header_bytes + message_bytes)

    reply = s.recv(4096)