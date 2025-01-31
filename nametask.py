from fastapi import FastAPI, HTTPException

app = FastAPI()

usernames = []


@app.post("/add_user/")
async def add_user(username: str):
    if not username:
        raise HTTPException(status_code=400, detail="Ім'я не може бути порожнім.")
    if username in usernames:
        raise HTTPException(status_code=400, detail="Ім'я вже додано.")
    usernames.append(username)
    return {"message": f"Ім'я {username} додано."}


@app.get("/get_usernames")
async def get_usernames():
    return {"usernames": usernames}


@app.delete("/delete_user")
async def delete_user(username: str):
    if not username:
        raise HTTPException(status_code=400, detail="Ім'я не може бути порожнім.")
    if username not in usernames:
        raise HTTPException(status_code=400, detail="Ім'я не знайдено.")
    usernames.remove(username)
    return {"message": f"Ім'я {username} видалено."}
