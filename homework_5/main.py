from fastapi import FastAPI, HTTPException, Header, Path, Query

app = FastAPI()


@app.get("/user/{user_id}")
async def user(
        user_id: int = Path(..., discription = "must be int."),
        timestamp: int = Query(..., dicription ="must be provided."),
        X_Client_Version: str = Header(..., discription ="The version of the client application.")
):
    if not isinstance(X_Client_Version, str):
        raise HTTPException(status_code=400, detail="X_Client_Version must be a string.")

    response = {
        "user_id": user_id,
        "timestamp": timestamp,
        "X_Client_Version": X_Client_Version,
        "message": f"Hello, {user_id}!"
    }
    return response


