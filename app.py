from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from models.base import Base

engine = create_engine('sqlite:///studysync.db')

Session = sessionmaker(bind=engine)
session = Session()