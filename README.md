# 📚 Research-Paper Summarizer & 🤖 ChatBot Suite

This project provides a full set of Python scripts and Streamlit apps that use **LangChain** with Hugging Face models to create AI-powered chatbots and research-paper summarizers.  
It demonstrates both simple command-line bots (with and without memory) and interactive web UIs for generating structured academic summaries.  
Users can select a research paper, preferred answer length, and tone, while the backend dynamically builds prompts and invokes a Hugging Face endpoint.  
The code is modular—separate files highlight how to use prompt templates, manage conversation history, and integrate with Streamlit for easy deployment.  
<h2>🎥 Demo Video</h2>
<p>Click the LinkedIn logo to watch the full demo:</p>
<a href="https://www.linkedin.com/posts/parth-mahadik_langchain-promptdesign-llm-activity-7374017256411803648-_J9g?utm_source=social_share_send&utm_medium=android_app&rcm=ACoAAEXfUkUBEnw0ueXBnKS10Irzgo9f874n2LE&utm_campaign=copy_link" target="_blank">
  <img src="https://static.vecteezy.com/system/resources/previews/018/930/480/large_2x/linkedin-logo-linkedin-icon-transparent-free-png.png" alt="LinkedIn Demo Video" width="120"/>
</a>
<p><strong>Video Link:</strong><br>
<a href="https://www.linkedin.com/posts/parth-mahadik_langchain-promptdesign-llm-activity-7374017256411803648-_J9g" target="_blank">
https://www.linkedin.com/posts/parth-mahadik_langchain-promptdesign-llm-activity-7374017256411803648-_J9g
</a></p>




---

## 📂 Project Structure
- **chat_bot_non_context.py** – Simple CLI chatbot without memory  
- **chat_bot_with_context.py** – CLI chatbot maintaining conversation history  
- **chat_prompt_template.py** – Demonstrates LangChain `ChatPromptTemplate` usage  
- **load_template_ui.py** – Streamlit app loading a saved JSON prompt template  
- **prompt_tamplate.py** – Streamlit summarizer with inline prompt template  
- **message.py** – Structured messaging with Human/System/AI messages

---


## 🛠️ Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-0E1116?style=for-the-badge&logo=chainlink&logoColor=white" />
  <img src="https://img.shields.io/badge/Hugging%20Face-FFDD00?style=for-the-badge&logo=huggingface&logoColor=black" />
  <img src="https://img.shields.io/badge/dotenv-000000?style=for-the-badge&logo=dotenv&logoColor=white" />
</p>

---

### 🔧 Horizontal Bar Overview
```text
Python ──────────────── ██████████████████████████
Streamlit ───────────── █████████████████████
LangChain ───────────── █████████████████████
Hugging Face Hub ────── █████████████████
dotenv ──────────────── ████████
