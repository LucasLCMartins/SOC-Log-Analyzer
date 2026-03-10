import re
import requests
import json
import csv

API_KEY = "SUA_CHAVE_AQUI"  # Substitua pela sua chave da AbuseIPDB
TELEGRAM_TOKEN = "SEU_TOKEN_AQUI"
CHAT_ID = "seu_chat_id_aqui"  # Substitua pelo seu chat ID do Telegram
LOG_FILE = 'access.log'

def extrair_ips(arquivo):
    try:
        with open(arquivo, 'r') as f:
            conteudo = f.read()
            ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', conteudo)
            return set(ips)
    except FileNotFoundError:
        print(f"❌ Erro: O arquivo {arquivo} não foi encontrado.")
        return set()

def verificar_reputacao(ip):
    url = 'https://api.abuseipdb.com/api/v2/check'
    query = {'ipAddress': ip, 'maxAgeInDays': '90'}
    headers = {'Accept': 'application/json', 'Key': API_KEY}
    
    try:
        response = requests.get(url, headers=headers, params=query)
        if response.status_code == 200:
            data = response.json()['data']
            return (
                data.get('abuseConfidenceScore', 0),
                data.get('usageType', 'N/A'),
                data.get('countryCode', '??')
            )
    except Exception as e:
        print(f"❌ Erro ao consultar IP {ip}: {e}")
    return None, None, None

def enviar_alerta_telegram(ip, score, pais, tipo):
    # Só envia alerta se o score for maior que 50%
    if score < 50:
        return

    mensagem = (f"🚨 *ALERTA DE SEGURANÇA*\n\n"
                f"⚠️ Tentativa Suspeita!\n"
                f"🌐 *IP:* `{ip}`\n"
                f"📊 *Score:* {score}%\n"
                f"🌍 *Origem:* {pais}\n"
                f"🖥️ *Tipo:* {tipo}")
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": mensagem, "parse_mode": "Markdown"}
    
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"❌ Erro no Telegram: {e}")

def salvar_relatorio(resultados):
    with open('relatorio_seguranca.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['IP', 'Score %', 'Tipo', 'Pais', 'Status'])
        writer.writerows(resultados)
    print("\n[+] Relatório 'relatorio_seguranca.csv' gerado com sucesso!")

# --- EXECUÇÃO DO SCRIPT ---
if __name__ == "__main__":
    print(f"--- Iniciando análise de: {LOG_FILE} ---")
    lista_ips = extrair_ips(LOG_FILE)
    dados_relatorio = []

    for ip in lista_ips:
        score, tipo, pais = verificar_reputacao(ip)
        
        if score is not None:
            status = "⚠️ MALICIOSO" if score > 50 else "✅ SEGURO"
            print(f"IP: {ip:15} | Score: {score}% | Status: {status}")
            
            enviar_alerta_telegram(ip, score, pais, tipo)
            
            dados_relatorio.append([ip, score, tipo, pais, status])
    
    if dados_relatorio:
        salvar_relatorio(dados_relatorio)
    
    print("--- Fim da análise ---")