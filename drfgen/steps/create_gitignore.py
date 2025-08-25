

def create_gitignore(project_path):
    gitignore_path = project_path / ".gitignore"
    if not gitignore_path.exists():
      

        gitignore_content = '''\
# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
*.pyc

# Virtual environment
venv/
.env/
.env.*

# Django stuff
*.log
db.sqlite3
media/
staticfiles/

# VSCode
.vscode/
.vscode

# IDEs
.idea/
*.sublime-workspace
*.sublime-project

# MacOS
.DS_Store

# Coverage reports
htmlcov/
.coverage
.tox/
.nox/
.coverage.*
.cache
.pytest_cache/

# Migrations (optional if you want to recreate them manually)
**/migrations/**/ __pycache__/
**/migrations/**/ *.pyc
**/migrations/**/ *.pyo
**/migrations/**/ *.pyd
# Uncomment the line below if you don't want to track migration files
# **/migrations/*.py

# Build
build/
dist/
*.egg-info/

# JWT tokens or private keys (if you store them locally)
*.pem
# *.key

# Other
logs/
tmp/
*.sqlite3
*.db
*.env
.env.*
.pytest_cache/
.mypy_cache/
.ruff_cache/
.pyre/
.ruff_cache/
.pytype/
.mypy_cache/
.pyre/
.pytype/

'''
        gitignore_path.write_text(gitignore_content)
        print(f"Created .gitignore at {gitignore_path}")
        return True
    else:
        print(f".gitignore already exists at {gitignore_path}, skipping creation.")
        return False  