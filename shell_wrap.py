import os, socket, telnetlib

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = telnetlib.TELNET_PORT  # Port to listen on (non-privileged ports are > 1023)


def wrap():
    os.popen()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
    wrap()

if __name__ == "__main__":
    main()