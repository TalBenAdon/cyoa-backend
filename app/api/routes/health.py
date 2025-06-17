from fastapi import APIRouter
from app.utils.db_tables_call_testing import log_and_return_all_tables
router = APIRouter()

@router.get("/healthz", status_code=204)
async def healthz():
    return

# lying for now
@router.get("/ready")
async def ready():
    return {"message": "ready"}

@router.get("/database")
async def database():
    log_and_return_all_tables()
    return {"message" : "action performed"}
    