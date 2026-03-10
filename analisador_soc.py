import re
import requests
import json

API_KEY = "SUA KEY AQUI"  # Substitua pela sua chave da AbuseIPDB
LOG_FILE = 'access.log'

def extrair_ips(arquivo):
    
    with open(arquivo, 'r') as f:
        conteudo = f.read()
        ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', conteudo)
    return set(ips)


def verificar_reputacao(ip):
    url = 'https://api.abuseipdb.com/api/v2/check'
    querystring = {'ipAddress': ip, 'maxAgeInDays': '90'}
    headers = {'Accept': 'application/json', 'Key': API_KEY}
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()['data']
        return data['abuseConfidenceScore'], data['usageType']
    return None, None

# --- EXECUÇÃO DO SCRIPT ---
print(f"--- Iniciando análise do arquivo: {LOG_FILE} ---")
lista_ips = extrair_ips(LOG_FILE)

for ip in lista_ips:
    score, tipo = verificar_reputacao(ip)
    if score is not None:
        status = "⚠️ MALICIOSO" if score > 50 else "✅ SEGURO"
        print(f"IP: {ip:15} | Score: {score}% | Tipo: {tipo} | Status: {status}")
    else:
        print(f"IP: {ip:15} | Falha na consulta.")

print("--- Fim da análise ---")

def verificar_reputacao(ip):
    url = 'https://api.abuseipdb.com/api/v2/check'
    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '90'
    }
    headers = {
        'Accept': 'application/json',
        'Key': API_KEY
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()['data']
        return data['abuseConfidenceScore'], data['usageType']
    return None, None

print(f"--- Iniciando análise do arquivo: {LOG_FILE} ---")
lista_ips = extrair_ips(LOG_FILE)

for ip in lista_ips:
    score, tipo = verificar_reputacao(ip)
    if score is not None:
        status = "⚠️ MALICIOSO" if score > 50 else "✅ SEGURO"
        print(f"IP: {ip:15} | Score: {score}% | Tipo: {tipo} | Status: {status}")

import csv

def salvar_relatorio(resultados):
    with open('relatorio_seguranca.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['IP', 'Confiança de Abuso (%)', 'Tipo de Uso', 'Status'])
        writer.writerows(resultados)
    print("\n[+] Relatório 'relatorio_seguranca.csv' gerado com sucesso!")
