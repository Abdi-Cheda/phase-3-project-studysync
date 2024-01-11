from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import argparse
from models.student import Student
from models.courses import Course
from models.schedule import Schedule
from models.base import Base


engine = create_engine('sqlite:///studysync.db')

Session = sessionmaker(bind=engine)
session = Session()
# Add more CLI functionality as needed...
# In app.py

def list_courses():
    courses = session.query(Course).all()
    for course in courses:
        print(f"{course.id}: {course.name}")

# Add argparse setup to call this function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="StudySync CLI")
    parser.add_argument("--list_courses", help="List all courses", action="store_true")

    args = parser.parse_args()

    if args.list_courses:
        list_courses()

Base.metadata.create_all(engine)