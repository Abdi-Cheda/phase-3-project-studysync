from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///studysync.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Student(Base):  # Model Definitions
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    def schedule(self):
        session = Session()
        schedules = session.query(Schedule).filter(Schedule.student_id == self.id).all()
        session.close()
        return schedules

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    course = Column(Integer)  # Changed from time to price
    day = Column(String)

    def schedules(self):
        session = Session()
        schedules = session.query(Schedule).filter(Schedule.course_id == self.id).all()
        session.close()
        return schedules

class Schedule(Base):
    __tablename__ = 'schedule'
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'))
    student_id = Column(Integer, ForeignKey('students.id'))
    time = Column(String)
    duration = Column(Integer)
    student = relationship("Student")
    course = relationship("Course")

Base.metadata.create_all(engine)

def create_student():
    session = Session()
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    student = Student(first_name=first_name, last_name=last_name)
    session.add(student)
    session.commit()
    session.close()
    print(f"Added student {first_name} {last_name}")

def create_course():
    session = Session()
    name = input("Enter course name: ")
    code = int(input("Enter course code: "))
    day = input("Enter day to take the course: ")
    course = Course(name=name, code=code, day=day)
    session.add(course)
    session.commit()
    session.close()
    print(f"Added course {name} {code} to be taken on {day}.")

def create_schedule():
    session = Session()
    student_id = int(input("Enter student ID: "))
    course_id = int(input("Enter course ID: "))
    time = input("Enter time for the course (e.g., 10:00 AM): ")
    duration = int(input("Enter duration in hours: "))

    schedule = Schedule(student_id=student_id, course_id=course_id, time=time, duration=duration)
    session.add(schedule)
    session.commit()
    session.close()
    print(f"Added schedule for Student ID {student_id} for Course ID {course_id} at {time} for {duration} hours")

    # Reminder Feature (simple version)
    print(f"Reminder: You have a course on {time} for {duration} hours.")


if __name__ == "__main__":
    while True:
        print("1. Add Student\n2. Add Course\n3. Add Schedule\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            create_student()
        elif choice == '2':
            create_course()
        elif choice == '3':
            create_schedule()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
