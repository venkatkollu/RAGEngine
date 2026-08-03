import shutil
import time
from pathlib import Path

from tqdm import tqdm

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

DOCUMENTS_DIR = "documents"
CHROMA_DIR = "chroma_db"
INDEX_FILE = "indexed_files.txt"

# --------------------------------------------------
# Load Indexed Files
# --------------------------------------------------

def load_indexed_files():

    if not Path(INDEX_FILE).exists():
        return set()

    with open(INDEX_FILE, "r") as f:

        return set(

            line.strip()

            for line in f

            if line.strip()

        )


def save_indexed_file(filename):

    with open(INDEX_FILE, "a") as f:

        f.write(filename + "\n")


# --------------------------------------------------
# Create / Load Chroma
# --------------------------------------------------

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

db = Chroma(
    persist_directory=CHROMA_DIR,
    embedding_function=embeddings,
)

indexed_files = load_indexed_files()

pdfs = list(Path(DOCUMENTS_DIR).glob("*.pdf"))

print("=" * 60)
print("Incremental PDF Ingestion")
print("=" * 60)
print(f"Found {len(pdfs)} PDF(s)\n")

all_chunks = []

splitter = RecursiveCharacterTextSplitter(

    chunk_size=500,

    chunk_overlap=100,

)

# --------------------------------------------------
# Read PDFs
# --------------------------------------------------

for pdf in pdfs:

    if pdf.name in indexed_files:

        print(f"✓ Skipping {pdf.name}")

        continue

    print(f"📄 Loading {pdf.name}")

    loader = PyMuPDFLoader(str(pdf))

    docs = loader.load()

    for doc in docs:

        doc.metadata["source"] = pdf.name

    chunks = splitter.split_documents(docs)

    all_chunks.extend(chunks)

    save_indexed_file(pdf.name)

print()

if len(all_chunks) == 0:

    print("No new PDFs found.")

    exit()

print(f"Created {len(all_chunks)} chunks")

# --------------------------------------------------
# Store in Chroma
# --------------------------------------------------

BATCH_SIZE = 50

start = time.time()

print("\nCreating embeddings...\n")

for i in tqdm(

    range(0, len(all_chunks), BATCH_SIZE),

    desc="Embedding",

):

    batch = all_chunks[i:i + BATCH_SIZE]

    db.add_documents(batch)

elapsed = time.time() - start

collection = db.get()

print()

print("=" * 60)

print("Finished")

print("=" * 60)

print(f"Time       : {elapsed:.2f} sec")
print(f"Documents  : {len(collection['documents'])}")
print(f"Vectors    : {len(collection['ids'])}")

print("=" * 60)