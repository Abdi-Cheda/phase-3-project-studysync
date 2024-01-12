from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from models.base import Base
from models.student import Student
from models.courses import Course
from models.schedule import Schedule

engine = create_engine('sqlite:///studysync.db')
Session = sessionmaker(bind=engine)

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
        raise
    finally:
        session.close()

def create_student(session):
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    student = Student(first_name=first_name, last_name=last_name)
    session.add(student)
    session.commit()
    print(f"Added student with ID {student.id}: {first_name} {last_name}")

def create_course(session):
    name = input("Enter course name: ")
    course = Course(name=name)
    session.add(course)
    session.commit()
    print(f"Added course with ID {course.id}: {name}")
    
def create_schedule():
    with session_scope() as session:
        student_id = int(input("Enter student ID: "))
        course_id = int(input("Enter course ID: "))
        time = input("Enter time for the course (e.g., 10:00 AM): ")
        duration = int(input("Enter duration in hours: "))

        # Fetch the student and course from the database
        student = session.query(Student).filter(Student.id == student_id).first()
        course = session.query(Course).filter(Course.id == course_id).first()

        if not student or not course:
            print("Invalid student ID or course ID.")
            return

        schedule = Schedule(student_id=student_id, course_id=course_id, time=time, duration=duration)
        session.add(schedule)

        print(f"Added schedule for Student ID {student_id} for Course ID {course_id} at {time} for {duration} hours")
        print(f"Reminder: Dear {student.first_name} {student.last_name}, you have course {course.name} {course.code} to be taken on {course.day} at {time} for a duration of {duration} hours.")


def main():
    Base.metadata.create_all(engine)

    while True:
        print("\n1. Add Student\n2. Add Course\n3. Add Schedule\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            create_student()
        elif choice == '2':
            create_course()
        elif choice == '3':
            create_schedule()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()