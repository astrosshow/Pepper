import openai
import os

print("pep_openai_model.py is being executed")
client = openai.Client()
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_response(prompt, model="gpt-4o-mini", max_tokens=100):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            stream=True
        )
        response_text = ""
        for chunk in response:
            if chunk.choices[0].delta.content:
                response_text += chunk.choices[0].delta.content
        return response_text.strip()
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I couldn't process your request."