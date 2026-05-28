from config import * 
from pathlib import Path
from git import Repo


def clone_repo(input_repo):
    repo = Repo.clone_from(input_repo, cloned_input_repo)
    return print(f"Repository cloned to: {cloned_input_repo}")