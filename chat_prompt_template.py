from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-V3.1",
    task = "text-generation",
    temperature = 0.7,
    
)
model = ChatHuggingFace(llm=llm)

chat_prompt = ChatPromptTemplate(
    [
        ("system","You are A expret {Domain}"),
        ("human","Explain about  {topic}")
        
    ]
)

prompt = chat_prompt.invoke(
    {
        "Domain":"Data Scitits",
        "topic":"Power Bi"

    }
)

result = model.invoke(prompt)
print(result.content)