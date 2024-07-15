from .database import SessionLocal
from .models import Message

def init_db():
    db = SessionLocal()
    predefined_messages = [
        {"user_message": "Hello", "bot_response": "Hi there! How can I help you today?"},
        {"user_message": "How are you?", "bot_response": "I'm just a bot, but I'm doing great! How about you?"},
        {"user_message": "What is your name?", "bot_response": "I am a chatbot created to assist you."},
        # Add more predefined messages here
    ]
    for msg in predefined_messages:
        db_message = db.query(Message).filter(Message.user_message == msg["user_message"]).first()
        if not db_message:
            new_message = Message(user_message=msg["user_message"], bot_response=msg["bot_response"])
            db.add(new_message)
    db.commit()
    db.close()
