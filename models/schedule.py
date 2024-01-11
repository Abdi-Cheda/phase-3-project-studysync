from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from .base import Base

class Schedule(Base):
    __tablename__ = 'schedules'

    id = Column(Integer, primary_key=True)

    # Relationships
    student = relationship("Student", back_populates="schedule")
    course = relationship("Course", back_populates="schedules")
