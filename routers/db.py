import chromadb

client = chromadb.EphemeralClient()
collection = client.get_or_create_collection("docs")