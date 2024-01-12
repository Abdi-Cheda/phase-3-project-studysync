from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from app import Session

# class Student(Base):
#     __tablename__ = 'students'

#     id = Column(Integer, primary_key=True)
#     schedule = relationship("Schedule", back_populates="student")





class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    # def schedule(self):
    #     session = Session()
    #     schedules = session.query(Schedule).filter(Schedule.student_id == self.id).all()
    #     session.close()
    #     return schedules