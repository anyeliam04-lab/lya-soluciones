import socket

def resolver_dns(dominio):
    try:
        ip = socket.gethostbyname(dominio)
        print(f"La IP de {dominio} es {ip}")
    except:
        print("No se pudo resolver el dominio.")

dominio = input("Introduce el dominio a auditar: ")
resolver_dns(dominio)

