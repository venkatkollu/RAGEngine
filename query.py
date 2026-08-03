from langchain_chroma import Chroma
from langchain_ollama import (
    OllamaEmbeddings,
    ChatOllama,
)

CHROMA_DIR = "chroma_db"

# --------------------------------------------------
# Embedding Model
# --------------------------------------------------

print("Loading embedding model...")

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# --------------------------------------------------
# Load Chroma Database
# --------------------------------------------------

print("Loading vector database...")

db = Chroma(
    persist_directory=CHROMA_DIR,
    embedding_function=embeddings,
)

retriever = db.as_retriever(
    search_type="similarity",
    search_kwargs={
        "k": 8
    },
)

# --------------------------------------------------
# LLM
# --------------------------------------------------

print("Loading LLM...")

llm = ChatOllama(
    model="gemma3:4b",
    temperature=0.3,
)

# --------------------------------------------------
# Prompt Builder
# --------------------------------------------------

def build_prompt(question, docs):

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    return f"""
You are an AI assistant that answers questions ONLY from the provided documents.

Rules:
- Answer only using the supplied context.
- Do not make up facts.
- If the answer is missing, reply exactly:
"I don't know based on the provided documents."

Context
-------
{context}

Question
--------
{question}

Answer
------
"""


# --------------------------------------------------
# Sources
# --------------------------------------------------

def print_sources(docs):

    print("\nRetrieved Sources")
    print("-" * 60)

    for i, doc in enumerate(docs, start=1):

        source = doc.metadata.get(
            "source",
            "Unknown",
        )

        page = doc.metadata.get(
            "page",
            "?",
        )

        print(
            f"{i}. {source} (Page {page})"
        )

    print("-" * 60)


# --------------------------------------------------
# Chat
# --------------------------------------------------

print("=" * 60)
print("📚 Personal Local RAG")
print("Type 'exit' to quit.")
print("=" * 60)

while True:

    question = input("\nQuestion: ").strip()

    if question.lower() in {
        "exit",
        "quit",
        "q",
    }:
        break

    docs = retriever.invoke(question)

    if len(docs) == 0:

        print("No relevant documents found.")

        continue

    print_sources(docs)

    prompt = build_prompt(
        question,
        docs,
    )

    response = llm.invoke(prompt)

    print("\nAnswer")
    print("-" * 60)
    print(response.content)
    print("-" * 60)