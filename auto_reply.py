import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_auto_reply(email_text, classification):
    prompt = f"""
Você é um assistente de e-mails. Gere uma resposta profissional e educada com base no seguinte e-mail e na sua classificação.

Classificação: {classification}
E-mail: {email_text}

Resposta:
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )

        reply = response['choices'][0]['message']['content'].strip()
        return reply

    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"
