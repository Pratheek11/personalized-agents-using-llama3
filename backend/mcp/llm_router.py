import ollama

async def summarize_text(prompt: str, instructions: list[str]) -> str:
    messages = [
        {"role": "user", "content": prompt}
    ]
    if instructions:
        messages.insert(0, {"role": "system", "content": " ".join(instructions)})
    response = ollama.chat(model="llama3", messages=messages)
    return response["message"]["content"]

async def generate_text(prompt: str) -> str:
    response = ollama.generate(model="llama3", prompt=prompt)
    return response['response']
