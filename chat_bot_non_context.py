from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-V3.1",
    task = "text-generation",
    temperature = 0.7,
    
)
model = ChatHuggingFace(llm=llm)

while True:
    user_input = input("You: ")
    if user_input == "exit":
        break

    result = model.invoke(user_input)
    print(f"AI: {result.content}")
