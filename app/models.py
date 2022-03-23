from . import db


class PropertyInfo(db.Model):
    __tablename__ = 'properties'

    prop_id = db.Column(db.INT(), primary_key=True)
    propTitle = db.Column(db.String(80))
    descr = db.Column(db.Text())
    rooms = db.Column(db.String(80))
    btroom = db.Column(db.String(80))
    price = db.Column(db.INT())
    pType = db.Column(db.String(80))
    location = db.Column(db.String(80))


    def __init__(self, propTitle,descr,rooms,btroom,price,pType,location):
        self.propTitle=propTitle
        self.descr=descr
        self.rooms=rooms
        self.btroom=btroom
        self.price=price
        self.pType=pType
        self.location=location

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
        return '<Property %r>' % (self.propTitle)
