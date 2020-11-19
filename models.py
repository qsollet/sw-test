from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base
import datetime

class Shorturl(Base):
    __tablename__ = 'shorturls'
    id = Column(String(6), primary_key=True, nullable=False)
    url = Column(String(50), nullable=False)
    accessed = Column(Integer, default=0)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __init__(self, id=None, url=None):
        self.id = id
        self.url = url

    def __repr__(self):
        return '<Shorturl %s -- %s>' % (self.id, self.url)
