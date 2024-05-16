from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/api/v1",
    tags=["Hello"]
)

@router.get('/ping')
async def ping():
    return JSONResponse(content={'text': 'trololo'})