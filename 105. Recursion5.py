import sys

def main():
    print(sys.getrecursionlimit())
    sys.setrecursionlimit(2000)
    print(sys.getrecursionlimit())

if __name__ == "__main__":
    main()
    