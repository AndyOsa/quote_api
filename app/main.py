from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, crud
from app.database import SessionLocal, init_db

app = FastAPI()

init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Quote API!"}

@app.get("/quotes", response_model=list[schemas.Quote])
def read_quotes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_quotes(db, skip=skip, limit=limit)

@app.get("/quotes/{quote_id}", response_model=schemas.Quote)
def read_quote(quote_id: int, db: Session = Depends(get_db)):
    quote = crud.get_quote(db, quote_id)
    if quote is None:
        raise HTTPException(status_code=404, detail="Quote not found")
    return quote

@app.post("/quotes", response_model=schemas.Quote)
def create_quote(quote: schemas.QuoteCreate, db: Session = Depends(get_db)):
    return crud.create_quote(db, quote)

@app.put("/quotes/{quote_id}", response_model=schemas.Quote)
def update_quote(quote_id: int, updated: schemas.QuoteCreate, db: Session = Depends(get_db)):
    quote = crud.update_quote(db, quote_id, updated)
    if quote is None:
        raise HTTPException(status_code=404, detail="Quote not found")
    return quote

@app.delete("/quotes/{quote_id}")
def delete_quote(quote_id: int, db: Session = Depends(get_db)):
    quote = crud.delete_quote(db, quote_id)
    if quote is None:
        raise HTTPException(status_code=404, detail="Quote not found")
    return {"detail": "Quote deleted"}

