from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .models import Base, Message
from pydantic import BaseModel
from .initial_data import init_db

Base.metadata.create_all(bind=engine)
init_db()

app = FastAPI()

class MessageCreate(BaseModel):
    user_message: str

class ChatCreate(BaseModel):
    user_message: str
    bot_response:str

class MessageResponse(BaseModel):
    user_message: str
    bot_response: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# User message sender endoint, if successful will return from the database
@app.post("/chat/", response_model=MessageResponse)
def create_message(message: MessageCreate, db: Session = Depends(get_db)):
    db_message = db.query(Message).filter(Message.user_message == message.user_message).first()
    if db_message:
        return {"user_message": db_message.user_message, "bot_response": db_message.bot_response}
    else:
        bot_response = f"I don't know the answer to '{message.user_message}' yet."  # Default response
        new_message = Message(user_message=message.user_message, bot_response=bot_response)
        db.add(new_message)
        db.commit()
        db.refresh(new_message)
        return {"user_message": new_message.user_message, "bot_response": new_message.bot_response}

# add predefined chats in the database 
@app.post("/addChat/", response_model=ChatCreate)
def create_chat(message: ChatCreate, db: Session = Depends(get_db)):
    db_message = db.query(Message).filter(Message.user_message == message.user_message).first()
    
    if db_message:
        return {"user_message": db_message.user_message, "bot_response": db_message.bot_response}
    else:
        new_message = Message(user_message=message.user_message, bot_response=message.bot_response)
        db.add(new_message)
        db.commit()
        db.refresh(new_message)
        
        return {"user_message": new_message.user_message, "bot_response": new_message.bot_response}

# stored chats fetched from database
@app.get("/messages/")
def read_messages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    messages = db.query(Message).offset(skip).limit(limit).all()
    return messages
