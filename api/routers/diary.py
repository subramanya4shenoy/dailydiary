from fastapi import APIRouter

router = APIRouter()

@router.get("/diary/{diary_page}")
def read_diary_page(diary_page):
    return { "status": "ok", "requested": diary_page}

@router.post("/diary/{diary_page}")
def add_diary_page(diary_page):
    return { "status": "ok", "requested": diary_page}

@router.put("/diary/{diary_page}")
def update_diary_page(diary_page):
    return { "status": "ok", "requested": diary_page}

@router.delete("/diary/{diary_page}")
def remove_diary_page(diary_page):
    return { "status": "ok", "requested": diary_page}