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

paper_input = st.selectbox("Select Research Paper name",["Attention Is All You Need -  Vaswani et al., 2017" , "ImageNet Classification with Deep Convolutional Neural Networks -Krizhevsky et al., 2012"," The Hallmarks of Cancer - Hanahan & Weinberg, 2000 (updated 2011)","CRISPR-Cas9 Mediated Genome Engineering - Jinek et al., 2012","Climate Change 2021: The Physical Science Basis – IPCC Working Group I Report"])
length_input = st.selectbox("Select Lenth of answer ",["Short (1-2 paragraphs)","Medium (3-5 paragraphs)","Long (detailed explanation)"])
style_input = st.selectbox("Select Explination Tone",["Beginner-Friendly","Technical","Code-Oriented", "Mathematical"])


template = PromptTemplate(
    template="""
You are an expert academic writer and technical communicator.

Please create a thorough and well-structured summary of the research paper titled "{paper_input}" using the following specifications:

Explanation Style: {style_input}  
Target Length: {length_input}

Guidelines for the Summary:
1. **Comprehensive Overview**  
   - Begin with a brief but clear statement of the paper’s main objective and its importance in the broader field.  
   - Identify the key research questions, hypotheses, or problems the authors set out to address.  
   - Describe the methodology, experimental setup, or theoretical framework in sufficient detail for an informed reader to understand the approach.

2. **Key Findings and Insights**  
   - Highlight the principal results, discoveries, or arguments.  
   - Explain why these findings matter and how they advance current knowledge or practice.

3. **Mathematical and Technical Details**  
   - Include any critical mathematical equations or algorithms when they are central to understanding the work.  
   - Present these equations in a clean, readable format and, where appropriate, illustrate the concepts with short, intuitive code snippets or pseudo-code to make them more approachable.

4. **Analogies and Intuitive Explanations**  
   - When concepts are complex, use clear analogies or real-world comparisons to simplify them without losing accuracy.  
   - Make sure these analogies remain faithful to the technical content.

5. **Critical Perspective**  
   - Note any limitations, open questions, or potential future directions the authors mention.  
   - Avoid adding unsupported speculation; stick to what can be inferred from the text.

6. **Clarity and Accessibility**  
   - Ensure the final summary reads smoothly and logically, with appropriate transitions between sections.  
   - Match the requested style ({style_input}) and stay close to the target length ({length_input}) while preserving accuracy and nuance.

Important:  
If the paper does not provide certain information—for example, specific equations, data details, or conclusions—state clearly: "Insufficient information available" instead of guessing or inventing details.

Your goal is to deliver a balanced, precise, and reader-friendly summary that captures both the technical depth and the broader significance of the research.
"""
,

input_variables=["paper_input", "style_input", "length_input"]
)







if st.button("Summarize"):
    prompt = template.invoke(
    {
    "paper_input":paper_input,
    "length_input":length_input,
    "style_input":style_input

})
    result = model.invoke(prompt)
    st.write(result.content)
