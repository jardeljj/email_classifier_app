import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Configura a chave da API
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def generate_auto_reply(email_text):
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")
        prompt = f"""
        Você é um assistente de atendimento. Leia o e-mail abaixo e gere uma resposta educada, profissional e clara.

        E-mail recebido:
        {email_text}

        Resposta sugerida:
        """

        response = model.generate_content( 
            contents=prompt,
        )

        return response.text.strip()

    except Exception as e:
        return f"Erro ao gerar resposta: {e}"
