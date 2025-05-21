# classifier/train_model.py
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from nlp_utils import preprocess_text


# Dados simulados (você pode trocar por dados reais depois)
emails = [
    "Please update the status of my open support case.",  # Produtivo
    "I need help accessing the system, it's urgent.",      # Produtivo
    "Happy birthday, hope you have a great day!",          # Improdutivo
    "Thank you for your help!",                            # Improdutivo
    "There's an issue with the login module.",             # Produtivo
    "Wishing you all the best in your new role!",          # Improdutivo
]

labels = ["Produtivo", "Produtivo", "Improdutivo", "Improdutivo", "Produtivo", "Improdutivo"]

# Pré-processar textos
emails_cleaned = [preprocess_text(email) for email in emails]

# Pipeline: TF-IDF + Naive Bayes
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('nb', MultinomialNB())
])

model.fit(emails_cleaned, labels)

# Salvar o modelo treinado
with open('classifier/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Modelo treinado e salvo com sucesso!")
