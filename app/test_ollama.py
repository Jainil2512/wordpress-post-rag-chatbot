from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="llama3.2:3b",
    base_url="http://localhost:11434",
    temperature=LLM_TEMPERATURE,
)


response = llm.invoke(
    "Say hello in one short sentence."
)


print(response.content)