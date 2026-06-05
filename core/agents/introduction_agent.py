from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain.agents import create_agent
from core.RAG.embedding_chunking import query_chunks

llm = ChatOllama(model="llama3.1")

@tool
def search_codebase(question: str) -> str:
    """Searches the codebase for relevant code chunks based on a question using RAG retrieval."""
    results = query_chunks(question)
    return "\n\n".join(results["documents"][0])


def run_introduction_agent():
    """
    Runs the Introduction Agent using the new LangChain 1.x API.

    Flow:
    1. search_codebase is the tool the agent can call to query ChromaDB
    2. create_agent combines the LLM + tools + system prompt into an agent graph
    3. agent.invoke() runs the agent with a task — it loops until it has a final answer
    4. The agent decides on its own when to call search_codebase and when it has enough info
    """

    system_prompt = """You are a code analysis assistant. Your job is to analyze a codebase and provide:
    1. A summary of what the codebase does
    2. A flowchart of the architecture in mermaid format

    Use the search_codebase tool to look up relevant parts of the codebase before answering."""

    agent = create_agent(
        model=llm,
        tools=[search_codebase],
        system_prompt=system_prompt
    )

    result = agent.invoke({
        "messages": [{"role": "user", "content": "Analyze this codebase. Provide a summary of what it does and a flowchart of the architecture in mermaid format."}]
    })

    print(result["messages"][-1].content)
