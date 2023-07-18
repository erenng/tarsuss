from app import db
import bcrypt



class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    surname = db.Column(db.String(40), nullable=False)
    phone = db.Column(db.String(14), nullable=False, unique=True)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)

    def to_dict(self):
        data = {
            "name": self.name,
            "surname": self.surname,
            "phone": self.phone,
            "email": self.email,
        }
        return data

    def check_password(self, password):
        is_valid = bcrypt.checkpw(self.password, password)
        return is_valid

    def from_dict(self, data):
        for field in ['name', 'surname', 'phone', 'email', 'password']:
            if field in data:
                setattr(self, field, data[field])



def hash_password(password):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password.decode('utf-8')

def check_password():
    pass
