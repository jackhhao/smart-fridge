from database.db import DB
import datetime

me = DB.engine_db

class Ingredient(me.Document):
    meta = {'collection': 'ingredients'}
    name = me.StringField(required=True)
    picture = me.StringField(required=True) # maybe ImageField if PIL is installed
    entry_date = me.DateTimeField()
    exp_date = me.DateTimeField()