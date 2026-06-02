from config import * 
from pathlib import Path
from git import Repo


def clone_repo(input_repo):
    """
    Takes a GitHub repository URL as input and clones it to the local file system.
    """
    repo = Repo.clone_from(input_repo, cloned_input_repo)
    return print(f"Repository cloned to: {cloned_input_repo}")