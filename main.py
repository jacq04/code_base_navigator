from config import * 
from git import Repo
from codebase_navigator.scanner import * 

input_repo = input("Provide your GitHub repository URL:")
clone_repo(input_repo) 