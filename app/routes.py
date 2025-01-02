from fastapi import APIRouter, HTTPException
from app.models import Task
from typing import List

# simula um banco de dados
tasks_db = []

# cria um roteador para agrupar as notas
router = APIRouter()

# lista todas as tarefas
@router.get("/tasks", response_model=List[Task])
def list_tasks(): 
    return tasks_db

# adciona uma nova tarefa
@router.post("/tasks", response_model=Task)
def create_task(task: Task):
    tasks_db.append(task)
    return task

# Rota para atualizar uma tarefa existente
@router.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    if task_id < 0 or task_id >= len(tasks_db):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    tasks_db[task_id] = updated_task
    return updated_task

# Rota para deletar uma tarefa
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks_db):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    tasks_db.pop(task_id)
    return {"message": "Tarefa deletada com sucesso"}