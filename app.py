from flask import Flask, request, render_template
import os
import pickle
from classifier.nlp_utils import preprocess_text
import PyPDF2

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Carregar modelo treinado
with open('classifier/model.pkl', 'rb') as file:
    model_data = pickle.load(file)

vectorizer = model_data['vectorizer']
model = model_data['model']

# Função para classificar o email
def classify_email(email):
    email_cleaned = preprocess_text(email)
    email_vector = vectorizer.transform([email_cleaned])
    prediction = model.predict(email_vector)
    label = 'Produtivo' if prediction[0] == 1 else 'Improdutivo'
    return label


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
                        content += page.extract_text()
        elif email_text:
            content = email_text

        if content.strip():
            classification = classify_email(content)
            suggested_response = "Em breve..."  # Vai entrar o auto_reply.py depois
        else:
            classification = "Nenhum conteúdo fornecido."
            suggested_response = "Nenhuma resposta gerada."

        return render_template('index.html', result=classification, response=suggested_response, email=content)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
