from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.routes import router, tasks_db

app = FastAPI()

app.include_router(router)

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <html>
        <head>
            <title>Gerenciador de Tarefas</title>
        </head>
        <body>
            <h1>Bem-vindo ao Gerenciador de Tarefas!</h1>
            <ul>
    """
    for task in tasks_db:
        html_content += f"<li>{task.title} - {'Concluído' if task.completed else 'Pendente'}</li>"
    
    html_content += """
            </ul>
        </body>
    </html>
    """
    return html_content
