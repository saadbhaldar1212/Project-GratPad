from gratpad import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    u_uname = db.Column(db.String(length=100), nullable=False)
    u_email = db.Column(db.String(length=100), nullable=False, unique=True)
    u_pass = db.Column(db.String(length=100), nullable=False)
    u_repass = db.Column(db.String(length=100), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f'User("{self.u_uname}","{self.u_email}")'


class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    j_dateTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    j_title = db.Column(db.String(50), nullable=False)
    j_content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    def __repr__(self):
        return f'Journal("{self.j_dateTime}","{self.j_title}")'


'''
class Contact(db.Model):
    c_id = db.Column(db.Integer, primary_key=True)
    c_fname = db.Column(db.String(100), nullable=False)
    c_lname = db.Column(db.String(100), nullable=False)
    c_email = db.Column(db.String(100), nullable=False)
    c_msg = db.Column(db.String(200), nullable=False)



class Product(db.Model):
    p_id = db.Column(db.Integer, primary_key=True)
    p_name = db.Column(db.String(100), nullable=False)
    p_desc = db.Column(db.String(100), nullable=False)
    p_price = db.Column(db.Float, nullable=False)
    p_quant = db.Column(db.Integer, nullable=False)
    p_img = db.Column(db.String(100), nullable=False)


class Admin(db.Model):
    a_id = db.Column(db.Integer, primary_key=True)
    a_uname = db.Column(db.String(100), nullable=False)
    a_pass = db.Column(db.String(100), nullable=False)

'''
