from typing import List
from fastapi import Depends, FastAPI, Body, BackgroundTasks, status, HTTPException
from fastapi import Body, APIRouter

import sqlalchemy as db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (Table, Column, String, Integer, MetaData, select, func)
#from flask_sqlalchemy import SQLAlchemy

from ..lecture.lectureService import LectureService
from ..lecture.lectureEntity import Lecture
from ..lecture.registerLectureCommand import RegisterLectureCommand

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
async def lectureRegister(db: Session = Depends(get_db)):
    lecture = Lecture('python', 'python lecture is the best')
    lectureService = LectureService()
    lectureService.insert_lecture(db, lecture)
    return f'lecture is registered successfully. id is {lecture.id}'


@router.get('/lecture/{lecture_id}', tags=['lectures'])
def findLecture(lecture_id: int, db: Session = Depends(get_db)):
  lectureService = LectureService()
  return lectureService.find_lecture(db, lecture_id)

@router.delete('/lecture/{lectureId}', tags=['lectures'])
def deleteLecture(lectureId: int, db: Session = Depends(get_db)):
  lectureService = LectureService()
  lectureService.delete_lecture(db, lectureId)
  return "success"

@router.get('/lectures', tags=['lectures'])
def lectureList(db: Session = Depends(get_db)):
  lectureService = LectureService()
  result = lectureService.list_lecture(db)
  return result

@router.put('/lecture/{lectureId}', tags=['lectures'])
async def updateLecture(lectureId: int, db: Session = Depends(get_db)):
  lectureService = LectureService()
  lectureService.update_lecture(db, lectureId)

@router.post('/lecture/bulk/', tags=['lectures'], response_model=str)
async def bulkInsert(db: Session = Depends(get_db), commandList: List[RegisterLectureCommand] = Body(...)):
    lectureList: List[Lecture] = []    
    for command in commandList:
      lectureList.append(Lecture(command.lectureName, command.lectureDescription))
      print(command)
    lectureService = LectureService()
    lectureService.bulk_insert_lecture(db, lectureList)
    return "success"
  
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post('/lecture/security', tags=['lectures'])
async def lectureSecurity(token: String = Depends(oauth2_scheme)):
  return {"token": token}