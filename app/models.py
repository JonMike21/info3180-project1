from . import db


class AddedProperties(db.Model):
    __tablename__ = 'added_properties'#'user_profiles'

    id = db.Column(db.Integer, primary_key=True) #, unique=True
    title = db.Column(db.String(80))
    description = db.Column(db.String(1024))
    bedroomNum = db.Column(db.Integer)
    bathroomNum = db.Column(db.Integer)
    price = db.Column(db.String(80))
    type = db.Column(db.String(80))
    location = db.Column(db.String(80))
    photo = db.Column(db.String(80))
    
    

    def __init__(self, title, description, bedroomNum,bathroomNum,price,type,location,photo):
        self.title = title
        self.description = description
        self.bedroomNum = bedroomNum
        self.bathroomNum = bathroomNum
        self.price = price
        self.type = type
        self.location = location
        self.photo = photo



    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)