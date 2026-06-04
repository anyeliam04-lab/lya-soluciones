import os

def menu():
    print("--- NetAudit Pro v1.0 ---")
    print("1. Escaneo de red básico")
    print("2. Verificación de archivos")
    print("3. Salir")

if __name__ == "__main__":
    menu()
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        print("Iniciando escaneo... (Requiere nmap instalado)")
    else:
        print("Saliendo.")

