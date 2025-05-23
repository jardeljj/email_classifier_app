import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

# Baixar recursos necessários (executa uma única vez)
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

def preprocess_text(text):
    # Converter para minúsculas
    text = text.lower()

    # Remover pontuação
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenizar (para português, usamos Regex para pegar palavras)
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)

    # Remover stopwords
    stop_words = set(stopwords.words('portuguese'))
    tokens = [word for word in tokens if word not in stop_words]

    # Lematização (em inglês, por limitação do WordNetLemmatizer)
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return ' '.join(tokens)
