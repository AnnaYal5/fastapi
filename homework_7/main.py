from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, constr, Field

app = FastAPI()


class User(BaseModel):
    first_name: constr(min_length=2)
    last_name: constr(min_length=2)
    email: EmailStr
    password: constr(min_length=8)
    phone: str = Field(..., pattern=r'^\+?[1-9]\d{1,14}$')

@app.post("/registr")
async def registr(user: User):
    return {"message": "Користувач успішно зареєстрований", "user": user.dict()}



