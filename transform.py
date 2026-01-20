from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def transform(users):
    for user in users:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Você é um especialista em marketing bancário."
                },
                {
                    "role": "user",
                    "content": f"Crie uma mensagem curta (máx. 100 caracteres) para {user['name']} sobre investimentos."
                }
            ]
        )

        message = response.choices[0].message.content.strip()

        user["news"].append({
            "icon": "credit.svg",
            "description": message
        })

    return users
