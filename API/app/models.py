from sqlalchemy import Column, String, Text, Integer, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from .extensions import db

Base = declarative_base()

class UserAttribute(Base):
    __tablename__ = "user_attribute"
    __table_args__ = {'schema': 'public'}

    id = Column(String(36), primary_key=True, default='sybase-needs-something-here')
    name = Column(String(255), nullable=False)
    value = Column(String(255))
    user_id = Column(String(36), nullable=False)
    long_value_hash = Column(LargeBinary)
    long_value_hash_lower_case = Column(LargeBinary)
    long_value = Column(Text)


class Blog(db.Model):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(String(36), ForeignKey('user_attribute.id'), nullable=False)

    # Define relationships after both classes are declared
    # author = relationship("UserAttribute", backref=backref("blogs", lazy="dynamic"))
    # comments = relationship("Comment", backref=backref("blog", lazy="dynamic"))

class Comment(db.Model):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    blog_id = Column(Integer, ForeignKey('blog.id'), nullable=False)
    author_id = Column(String(36), ForeignKey('user_attribute.id'), nullable=False)

    # Define relationships after both classes are declared
    blog = relationship("Blog", backref=backref("comments", lazy="dynamic"))
    # author = relationship("UserAttribute", backref=backref("comments", lazy="dynamic"))
