from typing import List
from pydantic import BaseModel

class Page(BaseModel):
    title:str
    body:str

