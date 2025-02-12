from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class URLShorthand(Base):
    __tablename__ = "url_shorthands"

    id = Column(Integer, primary_key=True)
    shorthand = Column(String, index=True)
    url = Column(String)
    owner = Column(String, index=True)
