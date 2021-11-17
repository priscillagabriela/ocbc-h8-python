from datetime import datetime
from config import db, ma
from marshmallow import fields

class Avoregion(db.Model):
    __tablename__ = 'avoregion'
    regionid = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(100))
    avocados = db.relationship(
        'Avocado',
        backref='avoregion',
        cascade='all, delete, delete-orphan',
        single_parent=True,
        order_by='desc(Avocado.date)'
    )

class Avotype(db.Model):
    __tablename__ = 'avotype'
    typeid = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100))
    avocados = db.relationship(
        'Avocado',
        backref='avotype',
        cascade='all, delete, delete-orphan',
        single_parent=True,
        order_by='desc(Avocado.date)'
    )

class Avocado(db.Model):
    __tablename__ = 'avocado'
    avoid = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10))
    avgprice = db.Column(db.Integer)
    totalvol = db.Column(db.Integer)
    avo_a = db.Column(db.Integer)
    avo_b = db.Column(db.Integer)
    avo_c = db.Column(db.Integer)
    type = db.Column(db.Integer, db.ForeignKey('avotype.typeid'))
    regionid = db.Column(db.Integer, db.ForeignKey('avoregion.regionid'))

class AvoregionSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Avoregion
        sqla_session = db.session
        load_instance = True

    avocados = fields.Nested('AvoregionAvocadoSchema', default=[], many=True)

class AvoregionAvocadoSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    date = fields.Str()
    avgprice = fields.Int()
    totalvol = fields.Int()
    avo_a = fields.Int()
    avo_b = fields.Int()
    avo_c = fields.Int()
    type = fields.Int()
    regionid = fields.Int()

class AvotypeSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Avotype
        sqla_session = db.session
        load_instance = True

    avocados = fields.Nested('AvotypeAvocadoSchema', default=[], many=True)

class AvotypeAvocadoSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    date = fields.Str()
    avgprice = fields.Int()
    totalvol = fields.Int()
    avo_a = fields.Int()
    avo_b = fields.Int()
    avo_c = fields.Int()
    type = fields.Int()
    regionid = fields.Int()

class AvocadoSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Avocado
        sqla_session = db.session
        load_instance = True

    avoregion = fields.Nested("AvocadoAvoregionSchema", default=None)
    avotype = fields.Nested("AvocadoAvotypeSchema", default=None)


class AvocadoAvoregionSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    regionid = fields.Int()
    region = fields.Str()

class AvocadoAvotypeSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    typeid = fields.Int()
    type = fields.Str()