from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-V3.1",
    task = "text-generation",
    temperature = 0.7,
    
)
model = ChatHuggingFace(llm=llm)

message = [
    SystemMessage(content="Your Assitent is Here sir !.."),
    HumanMessage(content="Tell me about Chatrapati Shivaji Maharaj....")

]

result =model.invoke(message)

message.append(AIMessage(content=result.content))

print(message)


