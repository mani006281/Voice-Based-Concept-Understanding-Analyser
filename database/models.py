from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Text

from database.database import Base


class Evaluation(Base):
    __tablename__ = "evaluations"

    id = Column(Integer, primary_key=True, index=True)

    student_name = Column(String)

    concept = Column(String)

    transcript = Column(Text)

    similarity = Column(Float)

    feedback = Column(Text)