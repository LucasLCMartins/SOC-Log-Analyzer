# 🛡️ Analisador de Logs SOC - Threat Intelligence

Este projeto automatiza a triagem de endereços IP maliciosos a partir de logs de servidores (`access.log`), integrando inteligência de ameaças e automação de alertas.

## 🚀 Funcionalidades
- **Extração Automática:** Identifica padrões de IPv4 em arquivos de log usando Regex.
- **Threat Intelligence:** Consulta a API do **AbuseIPDB** para verificar o Score de Confiança de Abuso.
- **Automação de Alertas (SOAR):** Envia notificações instantâneas para um bot no **Telegram** quando um IP malicioso (>50%) é detectado.
- **Reporting:** Gera um relatório estruturado em `.csv` para auditoria e resposta a incidentes.

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **Bibliotecas:** `requests`, `re`, `csv`, `json`
- **API:** AbuseIPDB
- **Bot API:** Telegram

## 📋 Como utilizar
1. Clone o repositório:
   ```bash
   git clone [https://github.com/LucasLCMartins/Projeto-SOC.git](https://github.com/LucasLCMartins/Projeto-SOC.git)
