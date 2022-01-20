from sqlalchemy.orm import Session

from app.lecture.lectureEntity import Lecture


class LectureService:
  def insert_lecture(self, db: Session, lecture: Lecture):
    db.add(lecture)
    db.commit()