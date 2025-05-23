from flask import Flask, request, render_template
import os
import pickle
from classifier.nlp_utils import preprocess_text
import PyPDF2

# Carregar o modelo treinado (pipeline completo)
with open('classifier/model.pkl', 'rb') as file:
    model = pickle.load(file)

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
                with open(filepath, 'rb') as f:
                    reader = PyPDF2.PdfReader(f)
                    for page in reader.pages:
                        content += page.extract_text() or ""
        elif email_text:
            content = email_text

        if content:
            email_clean = preprocess_text(content)
            prediction = model.predict([email_clean])
            label = 'Produtivo' if prediction[0] == 1 else 'Improdutivo'
        else:
            label = "Nenhum conteúdo enviado."

        # (Deixe a resposta automática 'Em breve...' por enquanto)
        suggested_response = "Em breve..."

        return render_template('index.html', result=label, response=suggested_response, email=content)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
