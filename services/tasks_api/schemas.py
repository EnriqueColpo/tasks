from uuid import UUID
from pydantic import BaseModel
from models import TaskStatus
from typing import List


class CreateTask(BaseModel):
    title: str


class APITask(BaseModel):
    id: UUID
    title: str
    status: TaskStatus
    owner: str

    class ConfigDict:
        orm_mode = True


class APITaskList(BaseModel):
    results: List[APITask]

    class ConfigDict:
        orm_mode = True


class CloseTask(BaseModel):
    id: UUID
