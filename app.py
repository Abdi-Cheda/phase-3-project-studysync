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
    print(f"Added student with ID {student.id}: {first_name} {last_name}")

def create_course(session):
    name = input("Enter course name: ")
    code = int(input("Enter course code: "))
    day = input("Enter day to take the course: ")
    course = Course(name=name, code=code, day=day)
    session.add(course)
    print(f"Added course with ID {course.id}: {name}")

def create_schedule():
    with session_scope() as session:
        students = session.query(Student).all()
        for i, student in enumerate(students, 1):
            print(f"{i}. {student.first_name} {student.last_name}")

        student_choice = int(input("Choose a student by number: "))
        selected_student = students[student_choice - 1]

        courses = session.query(Course).all()
        for i, course in enumerate(courses, 1):
            print(f"{i}. {course.name} (Code: {course.code})")

        course_choice = int(input("Choose a course by number: "))
        selected_course = courses[course_choice - 1]

        time = input("Enter time for the course (e.g., 10:00 AM): ")
        duration = int(input("Enter duration in hours: "))

        schedule = Schedule(student_id=selected_student.id, course_id=selected_course.id, time=time, duration=duration)
        session.add(schedule)

        print(f"Added schedule for Student {selected_student.first_name} {selected_student.last_name} for Course {selected_course.name} at {time} for {duration} hours")
        print(f"Reminder: Dear {selected_student.first_name} {selected_student.last_name}, you have course {selected_course.name} {selected_course.code} to be taken on {selected_course.day} at {time} for a duration of {duration} hours.")

def main():
    Base.metadata.create_all(engine)

    while True:
        print("\n1. Add Student\n2. Add Course\n3. Add Schedule\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            with session_scope() as session:
                create_student(session)
        elif choice == '2':
            with session_scope() as session:
                create_course(session)
        elif choice == '3':
            create_schedule()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()