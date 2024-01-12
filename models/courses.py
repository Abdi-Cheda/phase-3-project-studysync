from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from .base import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    schedules = relationship("Schedule", back_populates="course")
