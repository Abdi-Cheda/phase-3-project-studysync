from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    # Relationships
    schedule = relationship("Schedule", back_populates="student")
