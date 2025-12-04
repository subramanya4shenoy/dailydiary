from fastapi import FastAPI, HTTPException
from db.database import check_db_connetion
from routers import users, diary

app = FastAPI()

@app.get("/db-health")
def db_health():
    try:
        check_db_connetion()
        return { 'status': 'ok'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"db error {e}")

app.include_router(users.router)
app.include_router(diary.router)