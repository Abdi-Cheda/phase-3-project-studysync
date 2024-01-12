from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from app import Student
from app import Course

engine = create_engine('sqlite:///studysync.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()



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

    print(f"Reminder: You have a schedule at {time} for a duration of {duration} hours.")


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
