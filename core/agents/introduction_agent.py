from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from core.RAG.embedding_chunking import query_chunks

llm=ChatOllama(model="llama3.2")

@tool 
def search_codebase(question): 
    """Searches the codebased for relevant code chunks based on a question RAG retrival."""
    results = query_chunks(question)
    return "\n\n".join(results["documents"][0]) #chromaDB returns each possible emedign match as a list. LLM expects it as line by line
