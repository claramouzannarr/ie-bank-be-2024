from iebank_api import db
from datetime import datetime
import string, random

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    country = db.Column(db.String(64), nullable=False) 
    account_number = db.Column(db.String(20), nullable=False, unique=True)
    balance = db.Column(db.Float, nullable=False, default = 0.0)
    currency = db.Column(db.String(1), nullable=False, default="€")
    country = db.Column(db.String(100), nullable=False)  # Add country field here
    status = db.Column(db.String(10), nullable=False, default="Active")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Event %r>' % self.account_number

<<<<<<< HEAD
    def __init__(self, name, currency, country):
=======
    def __init__(self, name, country,currency):
>>>>>>> 86c5945c58957430bac44d413d69e5d05cfff7ae
        self.name = name
        self.country = country 
        self.account_number = ''.join(random.choices(string.digits, k=20))
        self.currency = currency
        self.balance = 0.0
        self.status = "Active"
        self.country = country