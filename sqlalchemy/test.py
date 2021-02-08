from sqlalchemy import Column,create_engine
from sqlalchemy.types import CHAR, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from random import randint
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session
from faker import Faker


fake = Faker('zh-cn')
url = "mysql+pymysql://root:123456@192.168.99.100:3306/sqlalchemy?charset=utf8"
engine = create_engine(
    url,
    echo=True,
    pool_size=8,
    pool_recycle=60*30
)
BaseModel = declarative_base(engine)
def init_db():
    BaseModel.metadata.create_all(engine)
def drop_db():
    BaseModel.metadata.drop_all(engine)

class User(BaseModel):
    __tablename__ = 'myuser'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    age = Column(Integer)

class Friendship(BaseModel):
    __tablename__ = 'friendship'
    id = Column(Integer, primary_key=True)
    user_id1 = Column(Integer, ForeignKey('myuser.id', ondelete='CASCADE', onupdate='CASCADE'))
    user_id2 = Column(Integer, ForeignKey('myuser.id', ondelete='CASCADE', onupdate='CASCADE'))


if __name__ == "__main__":
    # Friendship.metadata.create_all(engine)
    # init_db()

    # session = Session(engine)
    # for i in range(100):
    #     session.add(User(age=randint(1, 100),name=fake.name()))
    # session.flush() # 或 session.commit()，执行完后，user 对象的 id 属性才可以访问（因为 id 是自增的）
    # for i in range(100):
    #     session.add(Friendship(user_id1=randint(1, 100), user_id2=randint(1, 100)))
    # session.commit()
    # query1 = session.query(User.id,User.name).join(Friendship, User.id == Friendship.user_id1).all()
    # print(query1)

    n = "aaas".startswith('a')
    print((1-n))

    l = ['a','b','aa']


    m = list(filter(lambda x:bool(1-x.startswith('a')),l))
    print(m)
