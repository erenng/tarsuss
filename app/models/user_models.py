from app import db


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    surname = db.Column(db.String(40), nullable=False)
    phone = db.Column(db.String(14), nullable=False, unique=True)
    email = db.Column(db.String(40), nullable=False, unique=True)

    def to_dict(self):
        data = {
            "name": self.name,
            "surname": self.surname,
            "phone": self.phone,
            "email": self.email
        }
        return data

    def from_dict(self, data):
        for field in ['name', 'surname', 'phone', 'email']:
            if field in data:
                setattr(self, field, data[field])
