# 📧 Email Classifier + Auto Reply com IA

Uma aplicação web em Python que permite:
- ✅ Classificar e-mails como **Produtivo** ou **Improdutivo**.
- ✅ Gerar uma **resposta automática sugerida** utilizando IA (Google Gemini API).

---

## 🚀 Como executar localmente

### ✅ Pré-requisitos
- Python 3.10 ou superior instalado na máquina
- Conta na Google AI Studio para gerar uma chave da API Gemini

---

## ⚙️ Passos para rodar localmente

### 🔥 1. Clone o repositório
```bash
git clone https://github.com/jardeljj/email_classifier_app
cd email_classifier_app

```

### 🔥 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 🔥 3. Configure as variáveis de ambiente
```bash
Crie um arquivo chamado .env na raiz do projeto.
Adicione sua chave da API Gemini:
GEMINI_API_KEY=sua_chave_aqui
```

### ▶️ 4. Execute o projeto
python app.py

Acesse no navegador:
http://127.0.0.1:5000

### 🧠 Tecnologias utilizadas

   - Python + Flask
   - Scikit-Learn
   - Google Generative AI (Gemini API)
   - pdfplumber
   - NLTK
   - HTML + CSS