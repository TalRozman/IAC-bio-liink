from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from app.config import MONGO_URI

def connect_to_mongodb() -> tuple[bool,str]:
    """
        connect to mongo-db service.
        \nparam: 
        \n\tNone
        \nreturns: 
        \n\ttuple: (status: bool,message: str)
    """
    global logs
    try:
        mongo_client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
        mongo_client.admin.command('ping')
        db = mongo_client["logs_db"]
        logs = db["logs"]
        return (True, "Ping successful!")
    except Exception as e:
        return (False, f"Error connecting to MongoDB: {e}")