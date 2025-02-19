from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

books_db = []

@app.get("/get_books")
def get_books():

    return {
        "books": books_db
    }


@app.post("/create_book")
async def create_book(request: Request):
    data = await request.json()
    if "title" not in data or "author" not in data or "year" not in data:
        raise HTTPException(status_code=400, detail="Missing required fields")
    book_id = len(books_db) + 1
    new_book = {
        "id": book_id,
        "title": data["title"],
        "author": data["author"],
        "year": data["year"]

    }
    books_db.append(new_book)
    return new_book
