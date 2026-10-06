# RAG-Based PDF Question Answering System

An AI-powered PDF Question Answering application built using Retrieval-Augmented Generation (RAG).

The application allows users to upload a PDF, ask questions about its content, and receive concise answers based only on the information available in the uploaded document.

## 🚀 Features

- Upload PDF documents
- Extract text from PDF files
- Split documents into smaller chunks
- Generate semantic embeddings using Hugging Face
- Store and search document embeddings using ChromaDB
- Retrieve relevant information using semantic search
- Generate answers using Groq LLM
- Display relevant source pages
- Prevent duplicate source pages
- Simple and interactive Streamlit interface

## 🏗️ Architecture

PDF
   ↓
Text Extraction
   ↓
Document Chunking
   ↓
Hugging Face Embeddings
   ↓
ChromaDB Vector Database
   ↓
Similarity Search
   ↓
Relevant Context
   ↓
Groq LLM
   ↓
Answer + Sources

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- ChromaDB
- Hugging Face Sentence Transformers
- Groq API
- Retrieval-Augmented Generation (RAG)
- PyPDF

## 📁 Project Structure

```text
rag-pdf-qa/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
└── src/
    ├── __init__.py
    ├── config.py
    ├── llm.py
    ├── rag.py
    ├── embeddings.py
    └── vectorstore.py