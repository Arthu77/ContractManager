from app import db
from datetime import datetime

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    contracts = db.relationship('Contract', backref='category', lazy=True)

class Contract(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    number = db.Column(db.String(100), unique=True)
    party_a = db.Column(db.String(100))
    party_b = db.Column(db.String(100))
    sign_date = db.Column(db.Date)
    effective_date = db.Column(db.Date)
    expiry_date = db.Column(db.Date)
    value = db.Column(db.Float)
    status = db.Column(db.String(50))
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    attachments = db.relationship('Attachment', back_populates='contract', lazy=True, cascade="all, delete-orphan")

class ContractItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    specification = db.Column(db.String(200))
    unit = db.Column(db.String(50))
    quantity = db.Column(db.Float)
    unit_price = db.Column(db.Float)
    amount = db.Column(db.Float)
    contract_id = db.Column(db.Integer, db.ForeignKey('contract.id'), nullable=False)
    contract = db.relationship('Contract', backref='items')

class Attachment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), nullable=False)
    filepath = db.Column(db.String(500), nullable=False, unique=True)
    mimetype = db.Column(db.String(100))
    filesize = db.Column(db.Integer)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    contract_id = db.Column(db.Integer, db.ForeignKey('contract.id'), nullable=False)
    contract = db.relationship('Contract', back_populates='attachments')

    def __repr__(self):
        return f'<Attachment {self.filename}>'
