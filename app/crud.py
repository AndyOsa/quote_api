from sqlalchemy.orm import Session
from app import models, schemas
def get_quotes(db: Session, skip: int = 0, limit: int = 10);
  return db.query(models.Quote).offset(skip).limit(limit).all()
def get_quote(db: Session, quote_id: int):
  return db.query(models.Quote).filter(models.Quote.id == quote_id).first()
def create_quote(db: Session, quote: schemas.QuoteCreate):
  db_quote = models.Quote(
    text=quote.text, 
    author=quote.author,
    tags=",".join(quote.tags) if quote.tags else""
  )
  db.add(db_quote)
  db.commit()
  db.refresh(db_quote)
  return db_quote
def delete_quote(db: Session, quote_id: int):
  db_quote = get_quote(db, quote_id)
  if db_quote:
    db.delete(db_quote)
    db.commit()
  return db_quote
def update_quote(db:Session, quote_id: int, updated: schemas.QuoteCreate):
  db_quote = get_quote(db, quote_id)
  if not db_quote
    return None
  db_quote.text = updated.text
  db_quote.author = updated.author
  db_quote.tags = ",".join(updated.tags) if updated.tags else ""
  db.commit()
  db.refresh(db_quote)
  return db_quote
