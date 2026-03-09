# 🛡️ Log Threat Analyzer (SOC Automation)

Este projeto é uma ferramenta de automação para analistas de **SOC (Security Operations Center)** desenvolvida em Python. O objetivo é acelerar a triagem de incidentes ao identificar automaticamente IPs maliciosos em arquivos de log de servidores.

## 🚀 Funcionalidades
- **Extração via Regex:** Varre arquivos de texto (como o `access.log`) e extrai todos os endereços IPv4 válidos.
- **Threat Intelligence:** Consulta em tempo real a API do **AbuseIPDB** para verificar a reputação de cada IP.
- **Análise de Risco:** Exibe o score de confiança de abuso, o tipo de uso do IP (Data Center, ISP, etc.) e classifica o status como ✅ SEGURO ou ⚠️ MALICIOSO.

## 🛠️ Tecnologias e Ferramentas
- **Linguagem:** Python 3.x
- **Bibliotecas:** `requests` (para integração com API) e `re` (Expressões Regulares).
- **Integração:** AbuseIPDB API v2.
- **Controle de Versão:** Git e GitHub.

## 📂 Estrutura do Projeto
- `analisador_soc.py`: Script principal com a lógica de extração e consulta.
- `access.log`: Arquivo de exemplo contendo logs de servidor (simulando ataques e tráfego legítimo).

## 📖 Como Executar
1. Clone o repositório:
   ```bash
   git clone (git clone https://github.com/LucasLCMartins/log-threat-analyzer.git)
