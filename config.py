import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", "14298205"))
    API_HASH = os.environ.get("API_HASH", "28df6d84da76d8606bf5f0e71ecfb62c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6076895757:AAExdZXT7sLrNWMHhpMF6o-i2TK0XA1Wqm4") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "Forward_BOT") 
    OWNER_ID = os.environ.get("OWNER_ID", "1458235021")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://nakflixbot:alpha3720@cluster0.qjgcfs1.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "Forward_Session")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001870385542"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "SERIES_NETFLIXBOT")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
