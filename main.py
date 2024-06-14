from fastapi import FastAPI

from src import sub

app = FastAPI(
    title="fastapi-app"
)
app.include_router(sub.router)

@app.get("/")
async def root():
    return {"Hello": "World!"}