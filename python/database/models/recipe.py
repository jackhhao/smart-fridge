from database.db import DB
from database.models.ingredient import Ingredient
import datetime

me = DB.engine_db

class Recipe(me.Document):
    meta = {'collection': 'recipes'}
    name = me.StringField(required=True)
    picture = me.StringField(required=True)
    link = me.URLField()
    all_ingreds = me.ListField(Ingredient)
    avail_ingreds = me.ListField(Ingredient)
    needed_ingreds = me.ListField(Ingredient)
