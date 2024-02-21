from fastapi import FastAPI

from src.api.routers import all_routers
from src.schemas.city import CityAddDTO

app = FastAPI()

for router in all_routers:
    app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
