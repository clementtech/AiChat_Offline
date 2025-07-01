from ollama import chat

models = "mistral"

question = str(input("You: "))

stream = chat(
    model=models,
    messages=[{'role': 'user', 'content': question}],
    stream=True,
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
