from database.database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Test(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
