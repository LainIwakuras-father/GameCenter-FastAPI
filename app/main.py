import logging
import os

e
import uvicorn
from api.endpoints import router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="GamaCenterAPI", description="API к престоящему мероприятию", version="0.0.1")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],#замени на список доменов, которые могут обращаться к нашему API
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(router=router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)