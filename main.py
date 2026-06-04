#!/usr/bin/env python3
import os
import sys

def main_menu():
    while True:
        print("\n--- LYA Soluciones | Framework de Auditoría ---")
        print("1. Escáner de Puertos")
        print("2. Fuzzer de Archivos Sensibles")
        print("3. Analizador DNS")
        print("4. Salir")
        
        choice = input("\nSeleccione una opción: ")
        
        if choice == '1':
            target = input("Target IP/Host: ")
            os.system(f"python3 herramientas/port_scanner.py {target}")
        elif choice == '2':
            target = input("Target URL: ")
            # Usamos una ruta relativa desde la raíz
            os.system(f"python3 herramientas/fuzzer_senior.py {target} herramientas/config/wordlist.txt")
        elif choice == '3':
            target = input("Dominio: ")
            os.system(f"python3 herramientas/analizador_dns.py {target}")
        elif choice == '4':
            print("Cerrando sesión...")
            sys.exit()
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main_menu()

