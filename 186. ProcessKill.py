import psutil

def KillProcess(name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == name:
            print("Killing the process : ",name)
            proc.kill()

def main():
    KillProcess("Google Chrome")

if __name__ == "__main__":
    main()