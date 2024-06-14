from typing import List
from uuid import UUID

from pydantic import BaseModel

from models import TaskStatus


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
