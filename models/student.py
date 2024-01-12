from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    schedules = relationship("Schedule", back_populates="student")
