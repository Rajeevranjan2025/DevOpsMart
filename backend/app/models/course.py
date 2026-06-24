from sqlalchemy import Column, Integer, String, Float
from app.database.db import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    category = Column(String)
    provider = Column(String)
    price = Column(Float)
    rating = Column(Float)
    url = Column(String)