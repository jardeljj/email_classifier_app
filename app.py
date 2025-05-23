from flask import Flask, request, render_template
import os
from classifier.classifier import classify_email
from auto_reply import generate_auto_reply

import pdfplumber 
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    content = ""
    classification = None
    suggested_response = None

    if request.method == 'POST':
        uploaded_file = request.files.get('email_file')
        email_text = request.form.get('email_text')

        # Processamento de arquivos
        if uploaded_file and uploaded_file.filename != '':
            filepath = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(filepath)

            if uploaded_file.filename.endswith('.txt'):
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                except Exception as e:
                    content = f"Erro ao ler arquivo TXT: {e}"

            elif uploaded_file.filename.endswith('.pdf'):
                try:
                    with pdfplumber.open(filepath) as pdf:
                        for page in pdf.pages:
                            page_text = page.extract_text()
                            if page_text:
                                content += page_text + "\n"

                    if not content.strip():
                        content = "⚠️ Não foi possível extrair texto do PDF. Verifique se é um PDF com texto pesquisável, não imagem."

                except Exception as e:
                    content = f"Erro ao processar PDF: {e}"

        # Processamento de texto digitado
        elif email_text and email_text.strip() != '':
            content = email_text.strip()

        # Se há conteúdo, faz classificação e gera resposta
        if content and "Erro" not in content and "⚠️" not in content:
            classification = classify_email(content)
            suggested_response = generate_auto_reply(content)
        elif content.startswith("Erro") or content.startswith("⚠️"):
            classification = "❌ Não foi possível classificar"
            suggested_response = content  # Mostra o erro diretamente
        else:
            classification = "❌ Nenhum conteúdo recebido"
            suggested_response = "Nenhum conteúdo para gerar resposta."

        return render_template(
            'index.html',
            result=classification,
            response=suggested_response,
            email=content
        )

    return render_template('index.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
