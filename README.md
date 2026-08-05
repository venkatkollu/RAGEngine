# Personal Local RAG

> A fully local Retrieval-Augmented Generation (RAG) system built using Ollama, ChromaDB, LangChain, and Python.

---

# Overview

This project is a lightweight, fully offline RAG (Retrieval-Augmented Generation) system that allows users to ask natural language questions about their own PDF documents.

The system:

- Loads PDF documents
- Splits them into chunks
- Generates embeddings locally
- Stores vectors inside ChromaDB
- Retrieves relevant chunks
- Uses a local LLM through Ollama to answer questions

No cloud APIs are required.

---

# Objectives

The goal of this project is to create a personal AI assistant capable of searching and answering questions from private documents while running completely offline.

Current goals:

- Local execution
- No OpenAI API
- Private document search
- Fast semantic retrieval
- Easy to understand
- Easy to extend

---

# Current Version

Version: **1.0**

Status:

✅ Working

---

# Features

Current features include:

- PDF loading
- Automatic chunking
- Local embeddings
- Chroma vector database
- Semantic search
- Local LLM
- Source citation
- Incremental indexing by filename
- Fully offline

---

# Folder Structure

```
my-rag/

│

├── documents/

│      paper1.pdf

│      notes.pdf

│      resume.pdf

│

├── chroma_db/

│

├── indexed_files.txt

│

├── ingest.py

├── query.py

├── requirements.txt

└── README.md
```

---

# Technologies Used

## Language

- Python 3.14

---

## Vector Database

ChromaDB

Purpose:

- Store embeddings
- Similarity Search
- Persistent Storage

---

## LLM

Ollama

Current model:

```
smollm2:1.7b
```

Can later switch to

```
qwen3:8b
```

without changing the project.

---

## Embedding Model

```
nomic-embed-text
```

Advantages:

- Fast
- Small
- Good semantic retrieval
- Runs locally

---

## Document Loader

PyMuPDF

Reads

- PDFs
- Pages
- Metadata

---

## Text Splitter

RecursiveCharacterTextSplitter

Current configuration

```
chunk_size = 500

chunk_overlap = 100
```

---

# Pipeline

```
PDF

↓

PyMuPDF

↓

Pages

↓

Chunking

↓

Embeddings

↓

ChromaDB

↓

Retriever

↓

Prompt

↓

Ollama

↓

Answer
```

---

# Retrieval Flow

```
User Question

↓

Embedding

↓

Vector Search

↓

Top K Chunks

↓

Context

↓

LLM

↓

Answer
```

---

# Project Workflow

## Step 1

Place PDFs into

```
documents/
```

---

## Step 2

Run

```
python ingest.py
```

This will

- Read PDFs
- Chunk text
- Generate embeddings
- Store vectors

---

## Step 3

Run

```
python query.py
```

Ask questions such as

```
What is my CGPA?

Who authored this paper?

Summarize chapter 2.

Explain transformers.

What is attention?
```

---

# Embedding Process

```
PDF

↓

Text

↓

Embedding Model

↓

768 Dimension Vector

↓

Stored in ChromaDB
```

---

# Current Database

ChromaDB

Persistence

```
chroma_db/
```

Every embedding is stored locally.

---

# Incremental Indexing

Current implementation

```
indexed_files.txt
```

Example

```
resume.pdf

notes.pdf

research.pdf
```

When running

```
python ingest.py
```

Already indexed files are skipped.

---

# Prompt Strategy

Current prompt

- Use retrieved context
- Do not hallucinate
- Answer only from supplied documents
- Reply "I don't know" if information is missing

---

# Source Citation

Every answer also displays

```
Retrieved Sources

Resume.pdf

Page 2

Research.pdf

Page 4
```

This helps verify answers.

---

# Advantages

✔ Offline

✔ Free

✔ Private

✔ No API Keys

✔ Easy to understand

✔ Easy to extend

✔ Fast

---

# Current Limitations

Current version does NOT support

- Updating modified PDFs
- Deleting removed PDFs
- Keyword Search
- OCR
- Images
- Tables
- Reranking
- Web UI
- API
- Multi-user
- Cloud deployment

---

# Future Improvements

Version 2

- SHA256 Hash Indexing

Instead of filename

```
Resume.pdf
```

Store

```
Resume.pdf

Hash

A92B31...
```

Detect modified documents.

---

Version 3

SQLite Metadata

Store

- filename
- hash
- chunks
- date indexed

---

Version 4

Automatic Folder Watcher

```
documents/

↓

Watchdog

↓

Auto Index
```

No manual ingestion.

---

Version 5

Hybrid Search

```
Vector Search

+

Keyword Search
```

Better retrieval.

---

Version 6

Cross Encoder Reranker

```
Question

↓

Top 20 Chunks

↓

Cross Encoder

↓

Best 5 Chunks
```

Higher answer quality.

---

Version 7

Streaming Responses

Display tokens while generating.

Like ChatGPT.

---

Version 8

FastAPI Backend

```
POST /chat

POST /upload
```

---

Version 9

React Frontend

ChatGPT-like interface.

---

Version 10

Docker Deployment

Deploy anywhere.

---

Version 11

Mobile Application

Android

iOS

---

Version 12

Memory

Remember previous conversations.

---

Version 13

Multi-format Support

Support

- PDF
- DOCX
- TXT
- Markdown
- HTML
- CSV
- GitHub repositories

---

# Why ChromaDB?

For this project

ChromaDB is preferred because

- Extremely simple
- Fast setup
- Persistent
- Works locally
- Excellent LangChain integration
- Enough for thousands of documents

Qdrant is unnecessary at this stage.

---

# Why Ollama?

Benefits

- Runs locally
- No internet
- Free
- Supports many models
- Easy model switching

---

# Supported Models

Current

```
smollm2:1.7b
```

Recommended upgrades

```
qwen3:8b

gemma3:4b

deepseek-r1

llama3.1
```

---

# Future Vision

The long-term goal is to transform this project into a personal AI knowledge assistant.

Possible future capabilities include

- Personal document search
- Research assistant
- University notes assistant
- Code search
- Paper summarization
- Local AI memory
- Multi-device synchronization
- Voice interface
- Personal knowledge graph

---

# License

Personal Project

Open for learning and experimentation.

---

# Author

Built as a personal AI/RAG learning project using

- Python
- LangChain
- ChromaDB
- Ollama

```
Goal:

Learn Retrieval-Augmented Generation from scratch while building a useful real-world personal AI assistant.
```
