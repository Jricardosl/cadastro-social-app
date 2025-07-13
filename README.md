# Cadastro Social 📲

Sistema para cadastro de pessoas carentes em programas sociais, com backend em Python (Flask) e suporte à geração de PDFs com os dados da inscrição.

## 🚀 Funcionalidades

- Cadastro e login de usuários com senha criptografada.
- Formulário de inscrição com dados socioeconômicos.
- Armazenamento em banco de dados MySQL.
- Geração de PDF com informações da inscrição.
- Estrutura pronta para integração com app mobile (React Native/Expo).

---

## 🛠 Tecnologias

- **Backend:** Python, Flask
- **Banco de Dados:** MySQL
- **PDF:** ReportLab
- **Autenticação:** JWT + werkzeug
- **ORM:** SQL direto com MySQLdb (sem SQLAlchemy)

---

## ⚙️ Como Executar Localmente

### Pré-requisitos

- Python 3.8+
- MySQL instalado e rodando
- pip
- Virtualenv (opcional)

---

### 1. Clone o repositório

```bash
git clone https://github.com/Jricardosl/cadastro-social-app.git
cd cadastro-social-app/backend
