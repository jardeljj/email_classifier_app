import pickle
from .nlp_utils import preprocess_text

# Carrega o modelo treinado
with open('classifier/model.pkl', 'rb') as file:
    model = pickle.load(file)

def classify_email(email_text):
    """
    Classifica o texto do e-mail como 'Produtivo' ou 'Improdutivo'.
    """
    email_cleaned = preprocess_text(email_text)
    prediction = model.predict([email_cleaned])[0]

    if prediction == 1 or prediction == "1" or prediction == "Produtivo":
        return "Produtivo"
    elif prediction == 0 or prediction == "0" or prediction == "Improdutivo":
        return "Improdutivo"
    else:
        return str(prediction)  # fallback

