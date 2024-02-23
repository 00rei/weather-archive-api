from fastapi import FastAPI, Request

from src.api.routers import all_routers
from src.utils.parser import test

app = FastAPI()

for router in all_routers:
    app.include_router(router)


@app.post("/")
async def root(request: Request):
    print(await request.json())
    return 1


# if __name__ == "__main__":
#     test()
