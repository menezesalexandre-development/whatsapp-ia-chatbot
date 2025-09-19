<div align=center>
  <h1>ProsAI <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" alt="MADE WITH PYTHON"/></h1>
  <em>Chatbot de IA para WhatsApp, simples, automatizado e eficiente.</em>
</div>

<div align="center">
  <div style="display: flex; gap: 10px;" align="center">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
    <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/>
  </div>

  <img src="https://img.shields.io/badge/status-concluído-brightgreen" alt="Status"/>
</div>

## Índice
- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Como Usar](#como-usar)
- [Tecnologias](#tecnologias)
- [Contribuidores](#contribuidores)

## Descrição
O ProsAI é um chatbot de inteligência artificial integrado ao WhatsApp, desenvolvido para automatizar conversas e oferecer respostas inteligentes em tempo real, trazendo uma experiência de se usar os melhores assistentes virtuais dentro do app de mensagens mais difundido do mundo.

## Funcionalidades:
- Integração com o WhatsApp Web para envio e recebimento de mensagens.
- Sistema de histórico separado por contato, evitando mistura de conversas.
- Respostas automáticas utilizando IA via API (com suporte a múltiplos contatos com histórico individual).
- Endpoint em FastAPI/Flask para comunicação com o modelo de IA.

## Requisitos
Antes de começar, você precisa ter:
- Conta ativa em algum serviço de IA (recomendamos [OpenRouter](https://openrouter.ai/)).
- Uma **chave de API** válida (API Key), que deve ser configurada no projeto.
- Python 3.8+ instalado no computador.
- Dependências do projeto instaladas (via `requirements.txt`).
- Uma conta no WhatsApp para ser conectada.  

## Como Usar
Passo a passo de como executar o projeto:

### 1. Clone o repositório:
    git clone https://github.com/menezesalexandre-development/prosai-whatsapp-chatbot.git
    
### 2. Instale as dependências:
    pip install -r requirements.txt

### 3. Execute primeiro o `wpp.py`:
    python wpp.py 
  - O navegador será aberto automaticamente.
  - Escaneie o QR Code do WhatsApp Web com seu celular para conectar sua conta.
    <img src="https://github.com/user-attachments/assets/4e1f8bfc-7a95-4a8b-9e58-64c0b9454145" alt="WPP WEB LOGIN QRCODE PAGE" width=512 height=288/>

### 4. Execute o `main.py` para ativar a integração com a IA:
     python main.py

## Tecnologias
<div style="display: flex; gap: 10px;">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/>
</div>

## Contribuidores
- Alexandre Menezes – Desenvolvedor principal
