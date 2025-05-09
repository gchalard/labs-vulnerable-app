from sqlalchemy import Column, String, Boolean, BigInteger, ForeignKey, Integer
from sqlalchemy.orm import relationship
from .extensions import db

class UserEntity(db.Model):
    __tablename__ = "user_entity"
    __table_args__ = {'schema': 'public', 'extend_existing': True}

    id = Column(String(36), primary_key=True)
    email = Column(String(255))
    email_constraint = Column(String(255))
    email_verified = Column(Boolean, nullable=False, default=False)
    enabled = Column(Boolean, nullable=False, default=False)
    federation_link = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    realm_id = Column(String(255))
    username = Column(String(255))
    created_timestamp = Column(BigInteger)
    service_account_client_link = Column(String(255))
    not_before = Column(Integer, nullable=False, default=0)

class Blog(db.Model):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(db.Text, nullable=False)
    author_id = Column(String(36), ForeignKey('public.user_entity.id'), nullable=False)

    author = relationship("UserEntity", backref="blogs")

class Comment(db.Model):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True)
    content = Column(db.Text, nullable=False)
    blog_id = Column(Integer, ForeignKey('blog.id'), nullable=False)
    author_id = Column(String(36), ForeignKey('public.user_entity.id'), nullable=False)

    blog = relationship("Blog", backref="comments")
    author = relationship("UserEntity", backref="comments")