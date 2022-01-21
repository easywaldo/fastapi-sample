from sqlalchemy.orm import Session

from app.lecture.lectureEntity import Lecture


class LectureService:
  def insert_lecture(self, db: Session, lecture: Lecture):
    db.add(lecture)
    db.commit()

  def find_lecture(self, db: Session, lecture_id):
    lecture = db.get(Lecture, lecture_id)
    return lecture

  def delete_lecture(self, db: Session, lectureId):
    lecture = db.get(Lecture, lectureId)
    db.delete(lecture)
    db.commit()