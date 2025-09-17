from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

st.header("| Summarization of Research Papaer | ")

llm = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-V3.1",
    task = "text-generation",
    temperature = 0.7,
    
)

model = ChatHuggingFace(llm=llm)

user_input = st.text_input("")

if st.button("Summarize"):
    result=model.invoke(user_input)
    st.write(result.content)
