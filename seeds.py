from app import Session  # Adjust the import path as per your project structure
from models.courses import Course

def seed_data():
    session = Session()
    
    # Create some courses
    math = Course(name="Mathematics")
    science = Course(name="Science")
    
    # Add them to the session
    session.add(math)
    session.add(science)
    
    # Commit the session
    session.commit()

    print("Data seeded successfully.")
