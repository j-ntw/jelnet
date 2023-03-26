from telnetlib import Telnet

class Jelnet(Telnet):
    def __init__(self, host: str | None = None, port: int = 0) -> None:
        super().__init__(host, port)
        

def main():
    with Jelnet("127.0.0.1", 23) as jn:
        jn.interact()

if __name__ == "__main__":
    main()