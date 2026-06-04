#!/usr/bin/env python3
"""
NetAudit Pro - Advanced Infrastructure Fuzzer
Autor: anyeliam04-lab
Estatus: Senior Production Ready
"""

import os
import json
import requests
import time
import random
import sys

# Ruta base del script para evitar errores de ejecución
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class FuzzerSenior:
    def __init__(self, target):
        self.target = target.rstrip('/')
        self.session = requests.Session()
        # Simulación de navegador real para evitar bloqueos
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        })
        self.findings = []

    def load_wordlist(self, filepath):
        if not os.path.exists(filepath):
            print(f"[!] ERROR: Wordlist no encontrada en: {filepath}")
            sys.exit(1)
        with open(filepath, 'r') as f:
            return [line.strip() for line in f if line.strip()]

    def run(self, wordlist_path):
        paths = self.load_wordlist(wordlist_path)
        print(f"[*] Iniciando auditoría de infraestructura en: {self.target}")
        
        for path in paths:
            url = f"{self.target}{path}"
            try:
                # Usamos HEAD para eficiencia y sigilo
                response = self.session.head(url, timeout=5)
                if response.status_code == 200:
                    print(f"[CRÍTICO] Hallazgo detectado: {url} | Status: 200")
                    self.findings.append({"url": url, "status": 200})
                
                # Delay aleatorio para evasión de WAF (Web Application Firewall)
                time.sleep(random.uniform(0.3, 0.8)) 
            except requests.exceptions.RequestException:
                continue
        
        self.save_report()

    def save_report(self):
        report_dir = os.path.join(BASE_DIR, 'reports')
        os.makedirs(report_dir, exist_ok=True)
        
        safe_name = self.target.replace('https://', '').replace('http://', '').replace('/', '_')
        filename = os.path.join(report_dir, f"report_{safe_name}.json")
        
        with open(filename, 'w') as f:
            json.dump(self.findings, f, indent=4)
        print(f"[+] Auditoría completada. Reporte generado en: {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso correcto: python3 fuzzer_senior.py <url> <ruta_wordlist>")
        sys.exit(1)
    
    fuzzer = FuzzerSenior(sys.argv[1])
    fuzzer.run(sys.argv[2])
