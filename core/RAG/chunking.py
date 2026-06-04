from pathlib import Path
import ast
#should take the local repo path and then split and chunk. Main should only call once

EXCLUDED_DIRS = {".venv", "__pycache__", ".git"}

def get_python_files(repo_path):
    """
    Returns a list of paths to all .py files in the repo, excluding virtual envs and cache folders.
    """
    repo = Path(repo_path)
    return [
        file for file in repo.glob("**/*.py")
        if not any(part in EXCLUDED_DIRS for part in file.parts)
    ]

def chunk_file(file_path):
    """
    Parses a Python file using ast and returns a list of chunks,
    where each chunk is a dict with the code and metadata.
    """
    source = Path(file_path).read_text()
    tree = ast.parse(source)
    chunks = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            chunks.append({
                "code": ast.get_source_segment(source, node),
                "name": node.name,
                "type": "function" if isinstance(node, ast.FunctionDef) else "class",
                "file": str(file_path)
            })
    return chunks
