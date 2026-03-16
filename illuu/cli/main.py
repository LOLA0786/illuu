import sys

def main():
    if len(sys.argv) < 2:
        print("Illuu CLI\nUsage: illuu <command>")
        return

    cmd = sys.argv[1]

    if cmd == "version":
        import illuu
        print(f"illuu {illuu.__version__}")
    else:
        print(f"Unknown command: {cmd}")
