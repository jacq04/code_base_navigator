from config import *
from core.scanner import clone_repo
from core.RAG.chunking import get_python_files, chunk_file
from core.RAG.embedding_chunking import embed_store_chunks
from core.agents.introduction_agent import run_introduction_agent

input_repo = input("Provide your GitHub repository URL:")
clone_repo(input_repo)

python_files = get_python_files(cloned_input_repo)
all_chunks = []
for file in python_files:
    chunks = chunk_file(file)
    all_chunks.extend(chunks)

print(f"Total chunks: {len(all_chunks)}")
embed_store_chunks(all_chunks)
print("Chunks embedded and stored in ChromaDB.")

run_introduction_agent()