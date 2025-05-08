from main import app
from fastapi.responses import JSONResponse
from fastapi import Request
from app.exceptions import BaseAppException, InvalidAIResponse, OpenRouterAPIException, HasExistingAdventureException, AdventureNotFound

@app.exception_handler(BaseAppException)
async def base_exception_handler(request: Request, exc: BaseAppException):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.message
    )


@app.exception_handler(InvalidAIResponse)
async def invalid_AI_response_handler(request: Request, exc: InvalidAIResponse):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.message
    )


@app.exception_handler(OpenRouterAPIException)
async def open_router_API_exception(request: Request, exc: OpenRouterAPIException):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.message
    )
   
    
@app.exception_handler(HasExistingAdventureException)
async def open_router_API_exception(request: Request, exc: HasExistingAdventureException):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.message
    )
    
    
@app.exception_handler(AdventureNotFound)
async def open_router_API_exception(request: Request, exc: AdventureNotFound):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.message
    )
    