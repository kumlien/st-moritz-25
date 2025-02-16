import os  

class Config:  
    SECRET_KEY = os.environ.get('SECRET_KEY', 'the_default_secret_key')  
    # Add more configuration options as needed  
