
# I'm using sqlalchemy here to parallel django, but you can use whatever python
# library works for you, including doing your own serialization, using some
# NoSQL store, etc.
from sqlalchemy import create_engine, desc
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///nanoblog.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class NanoblogPost(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)

    @staticmethod
    def iter_all():
        session = Session()
        return session.query(NanoblogPost).order_by(
            desc(NanoblogPost.id))

    def addtodb(self):
        session = Session()
        session.add(self)
        session.commit()
