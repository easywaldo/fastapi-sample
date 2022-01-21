from fastapi import Depends, FastAPI, Body, BackgroundTasks, status, HTTPException
from fastapi import Body, APIRouter

import sqlalchemy as db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (Table, Column, String, Integer, MetaData, select, func)
#from flask_sqlalchemy import SQLAlchemy

from ..lecture.lectureService import LectureService
from ..lecture.lectureEntity import Lecture

from ..database import SessionLocal, engine

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
router = APIRouter()
engine = db.create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(bind = engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/lecture/register', tags=['lectures'])
async def lectureRegister():
    lecture = Lecture('python', 'python lecture is the best')
    session = Session()
    lectureService = LectureService()
    lectureService.insert_lecture(session, lecture)
    return f'lecture is registered successfully. id is {lecture.id}'


@router.get('/lecture/{lecture_id}', tags=['lectures'])
def findLecture(lecture_id: int, db: Session = Depends(get_db)):
  ##session = Session()
  lectureService = LectureService()
  return lectureService.find_lecture(db, lecture_id)

@router.delete('/lecture/{lectureId}', tags=['lectures'])
def deleteLecture(lectureId: int):
  session = Session()
  lectureService = LectureService()
  lectureService.delete_lecture(session, lectureId)
  return "success"

@router.get('/lecture/list', tags=['lectures'])
async def lectureList():
  session = Session()
  lectureService = LectureService()
  result = lectureService.list_lecture(session)
  return "test"