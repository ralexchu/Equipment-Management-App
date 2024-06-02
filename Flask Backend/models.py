from config import db

class User(db.Model):
    u_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), unique=False, nullable=False)
    last_name = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_json(self):
        return {
            'uId': self.u_id,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'email': self.email
        }

class Checkout(db.Model):
    u_id = db.Column(db.Integer, db.ForeignKey('user.u_id'), nullable=False)
    co_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_name = db.Column(db.String(120), unique=True, nullable=False)
    checkout_date = db.Column(db.Date, nullable=False)
    checkin_date = db.Column(db.Date, nullable=True)
    checkout_purpose = db.Column(db.String(255), nullable=False)

    def to_json(self):
        return {
            'uId': self.u_id,
            'coId': self.co_id,
            'itemName': self.item_name,
            'checkoutDate': self.checkout_date.isoformat() if self.checkout_date else None,
            'checkinDate': self.checkin_date.isoformat() if self.checkin_date else None,
            'checkoutPurpose': self.checkout_purpose
        }
class Checkin(db.Model):
    u_id = db.Column(db.Integer, db.ForeignKey('user.u_id'), nullable=False)
    ci_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_name = db.Column(db.String(120), unique=True, nullable=False)
    checkout_date = db.Column(db.Date, nullable=False)
    checkin_date = db.Column(db.Date, nullable=False)
    return_location = db.Column(db.String(255), nullable=False)
    cleaned_before_return = db.Column(db.Boolean, nullable=False)

    def to_json(self):
        return {
            'uId': self.u_id,
            'ciId': self.ci_id,
            'itemName': self.item_name,
            'checkoutDate': self.checkout_date.isoformat() if self.checkout_date else None,
            'checkinDate': self.checkin_date.isoformat() if self.checkin_date else None,
            'returnLocation': self.return_location,
            'cleanedBeforeReturn': self.cleaned_before_return
        }




















