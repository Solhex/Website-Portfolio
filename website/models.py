from . import db
from sqlalchemy.sql import func


class Article(db.Model):
    __bind_key__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    datetime_created = db.Column(db.DateTime(timezone=True), default=func.now())
    datetime_edited = db.Column(db.DateTime(timezone=True), default=func.now())
    datetime_posted = db.Column(db.DateTime(timezone=True), default=func.now())
    is_published = db.Column(db.Boolean, default=False)
    is_edited = db.Column(db.Boolean, default=False)
    is_deleted = db.Column(db.Boolean, default=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(512))
    content = db.Column(db.String(5000), nullable=False)

    def __repr__(self):
        return f'<Article {self.title}>'


class Subscription(db.Model):
    __bind_key__ = 'email_subscriptions'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    datetime_joined = db.Column(db.DateTime(timezone=True), default=func.now())
