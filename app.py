from flask import Flask, request, render_template
import os
from classifier.classifier import classify_email
from auto_reply import generate_auto_reply

from dotenv import load_dotenv

# Carregar as variáveis de ambiente (.env)
load_dotenv()

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files.get('email_file')
        email_text = request.form.get('email_text')

        content = ""
        if uploaded_file:
            filepath = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(filepath)
            if uploaded_file.filename.endswith('.txt'):
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            elif uploaded_file.filename.endswith('.pdf'):
                import PyPDF2
                with open(filepath, 'rb') as f:
                    reader = PyPDF2.PdfReader(f)
                    for page in reader.pages:
                        content += page.extract_text()
        elif email_text:
            content = email_text

        if content:
            classification = classify_email(content)
            suggested_response = generate_auto_reply(content, classification)
        else:
            classification = "Nenhum conteúdo recebido"
            suggested_response = "Nenhum conteúdo para gerar resposta"

        return render_template('index.html', result=classification, response=suggested_response, email=content)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
