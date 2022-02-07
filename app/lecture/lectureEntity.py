import sqlalchemy as db
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.sql.expression import select, text
from sqlalchemy.sql.schema import Sequence
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Lecture(db.Model):
    __tablename__ = "lecture"

    id = Column(Integer, primary_key=True, index=True)
    lectureName = Column(String, unique=True)
    lectureDescription = Column(String)

    def __init__(self, lectureName, lectureDescription):
      self.lectureName = lectureName
      self.lectureDescription = lectureDescription

    def update(self, lectureDescription):
      self.lectureDescription = lectureDescription