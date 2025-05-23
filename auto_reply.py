import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Configura a chave da API
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def generate_auto_reply(email_text):
    try:
        prompt = f"""
        Você é um assistente de atendimento. Leia o e-mail abaixo e gere uma resposta educada, profissional e clara.

        E-mail recebido:
        {email_text}

        Resposta sugerida:
        """

        response = client.models.generate_content(
            model="gemini-1.5-flash-latest",  # ou gemini-1.5-pro-latest se quiser mais qualidade
            contents=prompt,
        )

        return response.text.strip()

    except Exception as e:
        return f"Erro ao gerar resposta: {e}"
