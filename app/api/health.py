from fastapi import APIRouter

router = APIRouter()

@router.get("/healthz", status_code=204)
async def healthz():
    return

# lying for now
@router.get("/ready")
async def ready():
    return {"message": "ready"}
