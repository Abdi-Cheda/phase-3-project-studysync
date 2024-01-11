from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    # Relationships
    schedules = relationship("Schedule", back_populates="course")
