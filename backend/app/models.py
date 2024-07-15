from sqlalchemy import Column, Integer, String
from .database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    user_message = Column(String, unique=True, index=True)
    bot_response = Column(String)
