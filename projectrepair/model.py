from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash

engine = create_engine("mysql+pymysql://starlord:qwerty@127.0.0.1/toufique?host=localhost?port=3306", echo=True)
Base = declarative_base()

from sqlalchemy import Column, Integer, String
class Shop(Base):
    __tablename__ = 'shop'
    id = Column(Integer, primary_key=True)
    lati = Column(String)
    longi = Column(String)
    emailid = Column(String)
    phnno=Column(Integer)
    city=Column(String)
    state=Column(String)
    password=Column(String(128))  ## this must be hashed
    rating=Column(Integer)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)
    def selectAll(self):
        conn=engine.connect()
        res=conn.execute("select * from shop")
        lis=res.fetchall()
        ret={}
        for i in lis:
            k=i[0]
            v=i[1:]
            ret[k]=v
        return ret




