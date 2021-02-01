#coding:utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DATE,ForeignKey,CHAR #导入外键
from sqlalchemy.orm import  relationship  #创建关系
from sqlalchemy.orm import Session
from sqlalchemy import Column,create_engine
from sqlalchemy.types import CHAR, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from random import randint
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session
from faker import Faker


url = "mysql+pymysql://root:123456@192.168.99.100:3306/sqlalchemy?charset=utf8"
 
engine = create_engine(
    url,
    # echo=True,
    pool_size=8,
    pool_recycle=60*30
)
Base = declarative_base() #生成orm基类

# Company   Phone: 一对多
class Company(Base):

    __tablename__ = "company"

    name = Column(String(20),primary_key=True)
    location = Column(String(20))
  
    def __repr__(self):
        return "name:{0} location:{1}".format(self.name,self.location)
  
class Phone(Base):
     
    __tablename__ = "phone"

    id = Column(Integer,primary_key=True)
    model = Column(String(32))
    price = Column(String(32))
    company_name = Column(String(32),ForeignKey("company.name"))
    company = relationship("Company",backref="phone_of_company") 
  
    def __repr__(self):
        return "{0} model:{1}, price:{2}".format(self.id,self.model,self.price)

Base.metadata.create_all(engine) #创建表

session = Session(engine)
# ====================================================
# ## 插入数据 ##
# companys = {
#             "Apple":"Amercian",
#             "Xiaomi":"China",
#             "Huawei":"China",
#             "Sungsum":"Korea",
#             "Nokia":"Finland"
#            }
# phones = (
#         [1,"iphoneX","Apple",8400],
#         [2,"xiaomi2s","Xiaomi",3299],
#         [3,"Huaweimate10","Huawei",3399],
#         [4,"SungsumS8","SungSum",4099], 
#         [5,"NokiaLumia","Nokia",2399],
#         [6,"iphone4s","Apple",3800]
#          )        
# for key in companys:
#     new_company = Company(name=key,location=companys[key]) 
#     session.add(new_company)
# for phone in phones:
#     id = phone[0]
#     model = phone[1]
#     company_name = phone[2]
#     price = phone[3]
 
#     new_phone = Phone(id=id,model=model,company_name=company_name,price=price)
#     session.add(new_phone)
# ====================================================
# ## 正向查询 ##
# phone_obj = session.query(Phone).filter_by(model = 'iphoneX').first() #filter filter_by 区别
# print(phone_obj.company_name)
# print(phone_obj.company.location)   #通过relationship字段， 但是表结构中不用该字段创建结构
# print(phone_obj.company.name)
# ====================================================

# ## 反向查询 ##
company_obj = session.query(Company).filter(Company.name == "Nokia").first() #filter filter_by 区别
print(company_obj) 
print(company_obj.phone_of_company)
session.commit()
session.close()

# 通过join联表: 内联、外联
#     query = session.query(Food,Famous,Cook).join(Famous,Famous.food_name==Food.name).join(Cook,Cook.famous_name==Famous.famous).all()
# 通过外键联表
#     company_obj = session.query(Company).filter(Company.name == "Nokia").first() #filter filter_by 区别
#  with session.begin():  上下文