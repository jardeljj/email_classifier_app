import pickle
from .nlp_utils import preprocess_text


# Carrega o modelo treinado
with open('classifier/model.pkl', 'rb') as file:
    model = pickle.load(file)


def classify_email(email_text):
    """
    Classifica o texto do e-mail em uma categoria.
    
    Args:
        email_text (str): O texto do e-mail.
    
    Returns:
        str: A categoria prevista.
    """
    email_cleaned = preprocess_text(email_text)
    prediction = model.predict([email_cleaned])[0]
    return prediction
