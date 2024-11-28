import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai

def get_response(user_input):
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
            "role": "user",
            "content": user_input,
            }
        ]
)
    return completion.choices[0].message.content