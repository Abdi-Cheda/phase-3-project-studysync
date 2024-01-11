from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.student import Student
from models.course import Course
from models.schedule import Schedule

engine = create_engine('sqlite:///college.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Add more CLI functionality as needed...
