import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pickle
from classifier.nlp_utils import preprocess_text

# Baixar os recursos do NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Carregar dataset
data = pd.read_csv('dataset/emails.csv')

emails = data['email']
labels = data['label']  # 1 = produtivo, 0 = improdutivo

# Pré-processar os textos
emails_cleaned = [preprocess_text(email) for email in emails]

# Criar pipeline (vetorizador + modelo)
pipeline = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', MultinomialNB())
])

# Treinar
pipeline.fit(emails_cleaned, labels)

# Salvar o pipeline completo
with open('classifier/model.pkl', 'wb') as file:
    pickle.dump(pipeline, file)

print("✅ Modelo treinado e salvo como model.pkl")
