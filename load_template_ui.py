from langchain_core.prompts import PromptTemplate,load_prompt
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-V3.1",
    task = "test-generation",
    temperature=0.8
)


model = ChatHuggingFace(llm=llm)

paper_input = st.selectbox("Select Research Paper name",["Attention Is All You Need -  Vaswani et al., 2017" , "ImageNet Classification with Deep Convolutional Neural Networks -Krizhevsky et al., 2012"," The Hallmarks of Cancer - Hanahan & Weinberg, 2000 (updated 2011)","CRISPR-Cas9 Mediated Genome Engineering - Jinek et al., 2012","Climate Change 2021: The Physical Science Basis – IPCC Working Group I Report"])
length_input = st.selectbox("Select Lenth of answer ",["Short (1-2 paragraphs)","Medium (3-5 paragraphs)","Long (detailed explanation)"])
style_input = st.selectbox("Select Explination Tone",["Beginner-Friendly","Technical","Code-Oriented", "Mathematical"])


template = load_prompt("research_template.json")

if st.button("Summarize"):
    #invoking Template Prompt 
    prompt = template.invoke(
        {
    "paper_input":paper_input,
    "length_input":length_input,
    "style_input":style_input
        }
    )

    #invoking Model
    result = model.invoke(prompt)

    st.write(result.content)
    
