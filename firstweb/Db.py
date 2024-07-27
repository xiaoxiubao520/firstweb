# config.py  
  
class Config:  
    """基础配置"""  
    SECRET_KEY = "sfsdfsdfsdgjndsgsdgsdfsdfsfwefwewrwer" 
    SQLALCHEMY_DATABASE_URI = 'sqlite:///user.db'  # 示例为SQLite  
    SQLALCHEMY_TRACK_MODIFICATIONS = False  
    SQLALCHEMY_ECHO = True 
    DEBUG = True  
