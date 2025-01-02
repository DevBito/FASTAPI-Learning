from pydantic import BaseModel, Field

class Task(BaseModel):
    title: str
    description: str   
    completed: bool = Field(default=False)
