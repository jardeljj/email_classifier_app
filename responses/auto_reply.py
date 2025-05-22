# auto_reply.py

import openai

# Configure sua API Key da OpenAI
openai.api_key = ""

def gerar_resposta(email):
    prompt = f"""
    Você é um assistente de e-mails. Gere uma resposta educada, objetiva e profissional para o seguinte e-mail:

    "{email}"

    Resposta:
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",  # ou "gpt-3.5-turbo"
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.7
    )

    reply = response['choices'][0]['message']['content'].strip()
    return reply


if __name__ == "__main__":
    print("==== Gerador de Respostas ====\n")

    while True:
        email = input("Digite o conteúdo do email (ou 'sair' para encerrar):\n> ")
        if email.lower() == 'sair':
            break

        resposta = gerar_resposta(email)
        print(f"\nResposta sugerida:\n{resposta}\n")
