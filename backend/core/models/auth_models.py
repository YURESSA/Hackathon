from werkzeug.security import generate_password_hash, check_password_hash

from backend.core import db


class Role(db.Model):
    __tablename__ = 'roles'
    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), nullable=False, unique=True)

    users = db.relationship('User', backref='system_role', lazy=True)

    def __repr__(self):
        return f"<Role {self.role_name}>"



class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    university = db.Column(db.String(150), nullable=False)
    study_info = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    system_role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'), nullable=False)

    project_role = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "username": self.username,
            "full_name": self.full_name,
            "university": self.university,
            "study_info": self.study_info,
            "email": self.email,
            "phone": self.phone,
            "system_role": self.system_role.role_name,
            "project_role": self.project_role
        }
