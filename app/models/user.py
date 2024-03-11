from app import db
from datetime import datetime
import uuid

class User(db.Model):
    id = db.Column(db.String(50), primary_key=True, default=str(uuid.uuid4()))
    send = db.Column(db.Text, nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow)
    updatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<dmsModels {}>'.format(self.name)