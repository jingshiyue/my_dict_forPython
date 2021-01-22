from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import MetaData
from sqlalchemy.orm import mapper
from sqlalchemy.orm import Session
from faker import Faker
import random

fake = Faker('zh-cn')
url = "mysql+pymysql://root:123456@192.168.99.100:3306/sqlalchemy?charset=utf8"
engine = create_engine(
    url,
    echo=True,
    pool_size=8,
    pool_recycle=60*30
)
metadata = MetaData()  # 元数据

# 创建表
users_table = Table('users', metadata,
  Column('id', Integer, primary_key = True),
  Column('name', String(64)),
  Column('age', Integer),
  Column('address', String(64))
)
# metadata.create_all(engine) # 表的持久化
# users_table.create() # 方式二

# core查询，分为conn.execute、session.execute

# ########混合使用，用mapper映射##############
# # 定义类
# class User(object):
#     def __init__(self,name,fullname,password):
#         self.name = name
#         self.fullname = fullname
#         self.password = password

#     def __repr__(self):
#         return "<User('%s','%s','%s')>" % (self.name, self.fullname, self.password)

# # 映射类、表
# mapper(User, users_table)
# session = Session(engine)  # 建立会话
# session.add(User('ed','Ed Jones','edspassword'))
# session.commit()
# ######################


#######core 方式操作数据###############
# ## 增 ##
# conn = engine.connect()
# ins1 = users_table.insert().values(
#     name = fake.name(),
#     age = random.randint(20,50),
#     address = fake.address()
# )
# conn.execute(ins1)

# ## 删 ##
# from sqlalchemy import delete
# conn = engine.connect()
# dele = users_table.delete().where(users_table.c.age == 99)
# result = conn.execute(dele)
# print("结果数量 => %s" %result.rowcount)

# ## 改 ##
# from sqlalchemy import update
# conn = engine.connect()
# upd = users_table.update().values(age = 99).where(users_table.c.age == 20)
# result = conn.execute(upd)
# print("结果数量 => %s" %result.rowcount)



# ## 查 ##
from sqlalchemy.sql import select
from sqlalchemy import asc,desc
from sqlalchemy import func
from sqlalchemy import and_,or_,not_
conn = engine.connect()
# s = select([users_table])
# s = select([users_table.c.name,users_table.c.address]).where(users_table.c.name=='顾桂芝')
# s = select([users_table]).order_by(desc(users_table.c.age)).limit(10)
# s = select([func.sum(users_table.c.age).label('sum_age')])
# s = select([func.count(users_table.c.age).label('total_age')])
s = select([users_table]).where(
        # users_table.c.address.like('%北京%')
        and_(
            users_table.c.address.ilike('%北京%'),
            users_table.c.age < 50
        )
)   

rs = conn.execute(s)
# rs = rs.first()
# rs = rs.fetchall()
rs = rs.fetchall()
# rs = rs.fetchone()
print(rs)


######################