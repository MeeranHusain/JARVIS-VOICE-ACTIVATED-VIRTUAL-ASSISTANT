# from openai import OpenAI
# import os
# from dotenv import load_dotenv
# load_dotenv()
# openai_api_key = os.getenv("OPENAI_API_KEY")

# client = OpenAI(api_key=openai_api_key)

# response = client.chat.completions.create(
#     model="gpt-5.6-luna", 
#     messages=[
#         {"role": "system", "content": "your a virtual assistant named jarvis, you are a helpful assistant that can help with various tasks."},
#         {"role": "user", "content": "What is code completion in OpenAI API?"}
#     ]
# )

# print(response.choices[0].message.content)

# ====================================================================================

# import ollama

# response = ollama.chat(
#     model="llama3.1:8b",
#     messages=[
#         {
#             "role": "system",
#             "content": "your a virtual assistant named jarvis, you are a helpful assistant that can help with various tasks."
#         },
#         {
#             "role": "user",
#             "content": "What is coding?"
#         }
#     ]
# )

# print(response["message"]["content"])



# =====================================================================================


import os
from dotenv import load_dotenv
import ollama

load_dotenv()

api_key = os.getenv("OLLAMA_API_KEY")

client = ollama.Client(
    host="https://ollama.com",
    headers={
        "Authorization": f"Bearer {api_key}"
    }
)

response = client.chat(
    model="gpt-oss:20b-cloud",
    messages=[
        {
            "role": "system",
            "content": "You are Jarvis, a helpful virtual assistant."
        },
        {
            "role": "user",
            "content": "what is coding?"
        }
    ]
)

print(response["message"]["content"])


