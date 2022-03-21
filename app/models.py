from . import db


class PropertyInfo(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'properties'

    id = db.Column(db.INT(), primary_key=True)
    propTitle = db.Column(db.String(80))
    desc = db.Column(db.Text())
    rooms = db.Column(db.String(80))
    btroom = db.Column(db.String(80))
    price = db.Column(db.INT())
    pType = db.Column(db.String(80))
    location = db.Column(db.String(80))


    def __init__(self, propTitle,desc,rooms,btroom,price,pType,location):
        self.propTitle=propTitle
        self.desc=desc
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
