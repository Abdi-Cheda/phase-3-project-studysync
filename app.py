from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from models.student import Student
from models.courses import Course
from models.schedule import Schedule
from models.base import Base


engine = create_engine('sqlite:///studysync.db')

Session = sessionmaker(bind=engine)
session = Session()

class Student(Base): # Model Definitions
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    def schedule(self):
        return session.query(Schedule).filter(Schedule.student_id == self.id).all()
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String)
    day = Column(String)

    def schedules(self):
        return session.query(Schedule).filter(Schedule.course_id == self.id).all()

class Schedule(Base):
    __tablename__ = 'schedule'
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'))
    student_id = Column(Integer, ForeignKey('students.id'))
    time = Column(String)
    duration = Column(Integer)
    student = relationship("Student")
    course = relationship("Course")

Base.metadata.create_all(engine) # Create tables