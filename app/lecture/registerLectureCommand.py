from locale import strcoll
from pydantic import BaseModel
class RegisterLectureCommand(BaseModel):
    lectureName: str
    lectureDescription: str