import time
from ping3 import ping

def main():
    while(True):
        #Probar un size de 512
        result = ping('www.google.com', unit = 'ms', timeout=0.1, size=256)
        print (result)
        time.sleep(0.1)


if __name__ == "__main__":
    main()
