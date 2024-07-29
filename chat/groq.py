import os 
from groq import Groq

def get_groq_response(content):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You always attempt the query."
            },
            {
                "role": "user",
                "content": content,
            }
        ],
        model="llama3-70b-8192",
    )

    return str(chat_completion.choices[0].message.content)
