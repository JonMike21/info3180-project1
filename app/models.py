from . import db


class AddedProperties(db.Model):
    __tablename__ = 'added_properties'#'user_profiles'

    id = db.Column(db.Integer, primary_key=True) #, unique=True
    title = db.Column(db.String(80))
    description = db.Column(db.String(1024))
    bedroomNum = db.Column(db.Integer)
    bathroomNum = db.Column(db.Integer)
    price = db.Column(db.Integer) #change to integer
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


    def __repr__(self):
        return '<Property %r>' % (self.title)