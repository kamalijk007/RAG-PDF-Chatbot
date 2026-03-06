import pypdf
import chromadb

# Read PDF
reader = pypdf.PdfReader('data/your_document.pdf')
full_text = ""
for page in reader.pages:
    full_text += page.extract_text()

# Chunk it
chunks = []
for i in range(0, len(full_text), 300):
    chunks.append(full_text[i:i+300])

# Store in ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("bio_docs")
collection.add(
    documents=chunks,
    ids=[f"chunk_{i}" for i in range(len(chunks))]
)

print(f"Stored {len(chunks)} chunks in ChromaDB!")

