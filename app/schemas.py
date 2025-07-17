from pydantic import BaseModel
from typing import List, Optional
class QuoteBase(BaseModel):
  text: str
  author: str
  tags: Optional[List[str]] = []
  class QuoteCreate(QuoteBase):
    pass
  class QuoteCreate(QuoteBase);
    pass
  class Quote(QuoteBase):
    id: int
    class Config:
      orm_mode = True
    
