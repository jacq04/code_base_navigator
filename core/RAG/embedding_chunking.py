import chromadb

def embed_store_chunks(chunks):
    """
    Takes a list of chunk dicts and stores them in a ChromaDB collection.
    Each chunk is embedded automatically by ChromaDB using sentence transformers.
    """
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection(name="code_chunk_collection")

    for chunk in chunks:
        collection.add(
            documents=[chunk["code"]],
            metadatas=[{
                "name": chunk["name"],
                "type": chunk["type"],
                "file": chunk["file"]
            }],
            ids=[f"{chunk['file']}::{chunk['name']}"]
        )

def query_chunks(question, n_results=5):
    """
    Takes a natural language query and returns the most relevant code chunks from ChromaDB.
    """
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection(name="code_chunk_collection")

    results = collection.query(
        query_texts=[question],
        n_results=n_results
    )
    return results