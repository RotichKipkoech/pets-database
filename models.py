from datetime import datetime
from sqlalchemy.orm import validates
from app import db




# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
# db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    phonenumber = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    
    @validates('username')
    def validate_username(self, key, username):
        if len(username) < 5:
            raise ValueError('Username must be at least 5 characters')
        return username

    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError('Invalid email format. Must contain "@"')
        return email

    @validates('password')
    def validate_password(self, key, password):
        if not any(char.isdigit() for char in password):
            raise ValueError('Password must contain at least one digit')
        if not any(char.isupper() for char in password):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(char.islower() for char in password):
            raise ValueError('Password must contain at least one lowercase letter')
        return password

    @validates('phonenumber')
    def validate_phonenumber(self, key, phonenumber):
        if not str(phonenumber).isdigit() or len(str(phonenumber)) != 10:
            raise ValueError('Phone number must be exactly 10 digits')
        return phonenumber
    

class Veterinary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    location = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    services = db.relationship('Services', backref='veterinary', lazy=True)
    pets = db.relationship('Pets', backref='veterinary', lazy=True)
    
    @validates('name')
    def validate_name(self, key, name):
        if len(name) < 5:
            raise ValueError('Name must be at least 5 characters')
        if not name[0].isupper():
            raise ValueError('Name must start with an uppercase letter')
        return name


class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    services_type = db.Column(db.String(100), nullable=True)
    veterinary_id = db.Column(db.Integer, db.ForeignKey('veterinary.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    @validates('services_type')
    def validate_services_type(self, key, services_type):
        if len(services_type) < 5:
            raise ValueError('Name must be at least 5 characters')
        if not services_type[0].isupper():
            raise ValueError('Name must start with an uppercase letter')
        return services_type

class Pets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    veterinary_id = db.Column(db.Integer, db.ForeignKey('veterinary.id'), nullable=True)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    @validates('name')
    def validate_name(self, key, name):
        if len(name) < 5:
            raise ValueError('Name must be at least 5 characters')
        if not name[0].isupper():
            raise ValueError('Name must start with an uppercase letter')
        return name


class PetItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    
    @validates('item')
    def validate_item(self, key, item):
        if len(item) < 3:
            raise ValueError('Item must be at least 3 characters')
        if not item[0].isupper():
            raise ValueError('Item must start with an uppercase letter')
        return item
    
    @validates('price')
    def validate_price(self, key, price):
        if not isinstance(price, int):
            raise ValueError('Price must be an integer')
        return price
    

