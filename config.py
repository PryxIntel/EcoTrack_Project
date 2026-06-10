import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'ecotrack_super_secure_dev_key_123')
    
    # Replace this with your MongoDB Atlas string if deploying to the cloud later
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')
    DB_NAME = 'ecotrack_db'