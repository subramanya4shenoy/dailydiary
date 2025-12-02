from fastapi import FastAPI
from routers import users, diary

app = FastAPI()

@app.get("/health")
def health():
    return { 'status': 'ok'}


app.include_router(users.router)
app.include_router(diary.router)