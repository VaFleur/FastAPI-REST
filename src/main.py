import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.router import all_routers

app = FastAPI(title="Blog API")

for router in all_routers:
    app.include_router(router)

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)

# TODO починить апдейт
# TODO добавить удаление
# TODO добавить авторизацию по ЖВТ токену
# TODO убрать лишние зависимости
