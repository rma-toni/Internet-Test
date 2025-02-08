import time
from ping3 import ping
import os

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'

ENDC = '\033[0m'

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def print_results(counter, loss_counter):
    clear()
    
    print("\n-------------RMAF SOFTWARE-------------\n")

    percent = (loss_counter * 100) / counter

    if(percent <= 1 ):
        print(OKGREEN+"            Todo correcto!\n"+ENDC)
    elif(percent <= 2.5):
        print(WARNING+"         Inestabilidad leve\n"+ENDC)
    else:
        print(FAIL+"        Inestabilidad grave\n"+ENDC)


    print(f"Se perdieron {loss_counter} paquetes de {counter} enviados")


def main():

    counter = 0
    loss_counter = 0

    while(True):
        #Probar un size de 512
        result = ping('www.google.com', unit = 'ms', timeout=0.1, size=512)
        if(result == None):
            loss_counter += 1
        counter+=1
        time.sleep(0.1)
        
        if(counter % 10 == 0):
            print_results(counter, loss_counter)


if __name__ == "__main__":
    main()
