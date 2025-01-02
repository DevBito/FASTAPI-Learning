import sys
from pathlib import Path

# Adiciona o diretório raiz ao caminho de módulos
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.models import Task

task = Task(title="Fazer Coxinha", description="Aprender sobre fazer coxinha")

print(task)
print(task.dict())

