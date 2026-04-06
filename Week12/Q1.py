# ============================================================
#  WEEK 12 LAB — Q1: SCANNER INHERITANCE
#  COMP2152 — Phillip Onofua
# ============================================================

import socket
import urllib.request


class Scanner:
    def __init__(self, target):
        self.target = target
        self.results = []

    def display_results(self):
        print(f"Results for {self.target}:")
        if not self.results:
            print("  (no results)")
            return
        for result in self.results:
            print(f"  {result}")


class PortScanner(Scanner):
    def __init__(self, target, ports):
        super().__init__(target)
        self.ports = ports

    def scan(self):
        for port in self.ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            try:
                result = sock.connect_ex((self.target, port))
                if result == 0:
                    self.results.append(f"Port {port}: OPEN")
                else:
                    self.results.append(f"Port {port}: closed")
            finally:
                sock.close()


class HTTPScanner(Scanner):
    def __init__(self, target, paths):
        super().__init__(target)
        self.paths = paths

    def scan(self):
        for path in self.paths:
            try:
                response = urllib.request.urlopen(f"http://{self.target}{path}", timeout=1)
                self.results.append(f"{path} → {response.status} (accessible)")
            except Exception:
                self.results.append(f"{path} → NOT FOUND")


if __name__ == "__main__":
    print("=" * 60)
    print("  Q1: SCANNER INHERITANCE")
    print("=" * 60)

    print("\n--- Port Scanner ---")
    ps = PortScanner("127.0.0.1", [22, 80, 443])
    print(f"  Scanning {ps.target} ports...")
    ps.scan()
    ps.display_results()

    print("\n--- HTTP Scanner ---")
    hs = HTTPScanner("127.0.0.1", ["/", "/admin", "/.git/config"])
    print(f"  Scanning {hs.target} paths...")
    hs.scan()
    hs.display_results()

    print("\n" + "=" * 60)
