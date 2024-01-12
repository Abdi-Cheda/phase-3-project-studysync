from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from .base import Base

class Schedule(Base):
    __tablename__ = 'schedule'
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'))
    student_id = Column(Integer, ForeignKey('students.id'))
    time = Column(String)
    duration = Column(Integer)
    student = relationship("Student", back_populates="schedules")
    course = relationship("Course", back_populates="schedules")
