from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base
import random
import string

class Shorturl(Base):
    __tablename__ = 'shorturls'
    id = Column(String(6), primary_key=True, nullable=False)
    url = Column(String(50), nullable=False)
    accessed = Column(Integer, default=0)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __init__(self, url, id=None):
        # If no id is given then generate one that is not already set
        if id is None:
            while (id := self.generate_id()):
                if Shorturl.query.filter(Shorturl.id == id).first() == None:
                    break
        self.id = id
        self.url = url

    def __repr__(self):
        return '<Shorturl %s -- %s>' % (self.id, self.url)

    def generate_id(self, length=6):
        chars = string.ascii_letters + string.digits
        return ''.join(random.sample(chars, length))
