# 🤖 Chat Bot WhatsApp
Bot inteligente para WhatsApp desenvolvido com inteligência artificial, utilizando RAG (Retrieval-Augmented Generation) para respostas contextualizadas e precisas.
## 📋 Sobre o Projeto
Este projeto é um chatbot avançado para WhatsApp que utiliza técnicas modernas de IA para fornecer respostas inteligentes e contextualizadas. O bot é capaz de processar mensagens, buscar informações relevantes em uma base de conhecimento e gerar respostas personalizadas usando modelos de linguagem.

## ✨ Principais Características

* 🧠 IA Avançada: Utiliza LangChain para orquestração de LLMs
* 📚 RAG (Retrieval-Augmented Generation): Busca contextual em base de conhecimento vetorial
* 🗄️ ChromaDB: Armazenamento vetorial para recuperação eficiente de informações
* ⚡ API REST: Interface FastAPI para integração e comunicação
* 🐳 Docker: Containerização completa para fácil deployment
* 📱 [Waha](https://waha.devlike.pro/docs/integrations/python/): WhatsApp API

## 🛠️ Tecnologias Utilizadas
### Backend & Framework

* Python 3.x: Linguagem principal do projeto
* FastAPI: Framework web moderno e de alta performance para criação da API REST
* LangChain: Framework para desenvolvimento de aplicações com LLMs

### Inteligência Artificial

* LangChain: Orquestração de modelos de linguagem e chains
* ChromaDB: Banco de dados vetorial para armazenamento de embeddings
* RAG (Retrieval-Augmented Generation): Técnica para respostas contextualizadas

### Infraestrutura

* Docker: Containerização da aplicação
* Docker Compose: Orquestração de containers

## 🚀 Como Executar
### Pré-requisitos

* Docker e Docker Compose instalados
* Conta do WhatsApp para vincular ao bot

## Instalação com Docker (Recomendado)

### 1.Clone o repositório
### 2.Configure as variáveis de ambiente
``` cp .env.example .env ```

### 4.Inicie os containers
``` docker-compose up --build waha ```
``` docker-compose up --build api ```

### 5.Acesse a rota 'http://localhost:3000/dashboard/' no seu navegador

### 6.Acesse a opção da API

<img width="500" height="332" alt="waha1_apikey" src="https://github.com/user-attachments/assets/09dd69e7-e08c-4eb7-b254-534f0959ba4f" />

### 7.Insira sua WAHA_API_KEY e salve as alterações

<img width="500" height="472" alt="waha2_apikey" src="https://github.com/user-attachments/assets/2e65c808-db5a-433b-96df-6ab3c478c94c" />

### 8.Verifique se a API_KEY foi validada

<img width="500" height="408" alt="waha3_apikey" src="https://github.com/user-attachments/assets/425e2d67-294f-4ad3-a9f9-65d5744267ea" />

### 9.Acesse as configurações da sessão default

<img width="500" height="481" alt="waha1" src="https://github.com/user-attachments/assets/a1756a3e-9fae-40e7-b07b-b272480651e3" />

### 9.Selecione +Webhook

<img width="500" height="508" alt="waha2" src="https://github.com/user-attachments/assets/7c1e1def-2217-41b7-a1a2-9c447e0e7776" />

### 10.Desmarque a opção session.status

<img width="500" height="497" alt="waha3" src="https://github.com/user-attachments/assets/879f21ec-8e89-4418-9bcc-c7215d790ceb" />

### 11.Altere a URL para (http://api:5000/chatbot/webhook)

<img width="500" height="491" alt="waha3_5" src="https://github.com/user-attachments/assets/8ae52be6-5184-4e55-b3de-a0b22794d787" />

### 12.Selecione Update para salvar e atualizar as mudanças

<img width="500" height="509" alt="waha4" src="https://github.com/user-attachments/assets/fd1a8fd8-3ab5-478b-a864-ff2b122d6f00" />

### 13.Inicie a sessão default

<img width="500" height="508" alt="waha5" src="https://github.com/user-attachments/assets/d399ef01-cb6b-4d01-b222-976cb2be38d0" />

### 14.Selecione o Login para conectar receber escanear o QR Code com seu celular no WhatsAPP

<img width="500" height="499" alt="waha6" src="https://github.com/user-attachments/assets/fe3a0c4d-e08f-46f9-abaf-34920c8fb22a" />

### 14.Conexão bem sucedida, agora quando você receber uma mensagem, o Bot responderá as mensagens com base no contexto fornecido através do ChromaDB

<img width="500" height="493" alt="waha7" src="https://github.com/user-attachments/assets/a41757f8-38d6-4ce8-a51b-bb7e6c31234f" />


## 📚 Como Funciona
### Fluxo de Processamento

* Recepção de Mensagem: O bot recebe mensagens via WhatsApp
* Processamento: A mensagem é processada e enviada para a API FastAPI
* Busca Contextual: O sistema RAG busca informações relevantes no ChromaDB
* Geração de Resposta: O LangChain orquestra o LLM para gerar uma resposta contextualizada
* Envio: A resposta é enviada de volta ao usuário no WhatsApp

## 📞 Suporte
Se você encontrar algum problema ou tiver dúvidas, por favor abra uma issue.

