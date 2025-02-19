from fastapi import FastAPI, Request, HTTPException
import uvicorn

app = FastAPI()


users_db = [
    {"user_id": 1, "name": "Іван",   "group_id": 1, "active": True},
    {"user_id": 2, "name": "Марія", "group_id": 1, "active": False},
    {"user_id": 3, "name": "Олег",  "group_id": 2, "active": True},
    {"user_id": 4, "name": "Анна",  "group_id": 2, "active": True},
    {"user_id": 5, "name": "Максим","group_id": 3, "active": False}
]

@app.get("/users/{user_id}")
async def user(user_id = int)