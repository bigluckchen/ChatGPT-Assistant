from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# 连接到SQLite数据库
engine = create_engine('sqlite:///data/ielts.db?check_same_thread=False')

# 创建Base模型类
Base = declarative_base()

# 创建一个模型类
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    is_valid = Column(Integer)

class TestsPart1(Base):
    __tablename__ = 'tests_part1'

    id = Column(Integer, primary_key=True)
    topic = Column(String)
    question = Column(String)
    used_year = Column(Integer)
    used_month_start = Column(Integer)
    used_month_end = Column(Integer)
    is_valid = Column(Integer)

# 创建会话类
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":
    # 查询所有用户
    users = session.query(User).all()

    # 打印查询结果
    for user in users:
        print(user.username, user.password)
