from sqlalchemy import Column, Integet, String, Table, ForeignKey
from sqlachemy.orm import relationship, declarative_base
Base = declaratibe_base()
class Quote(Base):
  __tablename__ = "quotes"
  id = Column(Integer, primary_key=True, index=True)
  text = Column(String, nullable=False)
  author = Column(String, nullable=False)
  tags = Column(String)
