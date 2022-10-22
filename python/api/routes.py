from api import bp  # noqa
from database.models.recipe import Recipe
from database.models.ingredient import Ingredient
from pymongo.errors import DuplicateKeyError
# from flask_pymongo import PyMongo
# from flask_mongoengine import MongoEngine
from flask import Flask, request, url_for, jsonify
from bson.objectid import ObjectId
# from utils import config

@bp.errorhandler(404)
def resource_not_found(e):
    """
    An error-handler to ensure that 404 errors are returned as JSON.
    """
    return jsonify(error=str(e)), 404

@bp.errorhandler(DuplicateKeyError)
def resource_not_found(e):
    """
    An error-handler to ensure that MongoDB duplicate key errors are returned as JSON.
    """
    return jsonify(error=f"Duplicate key error."), 400

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.

@bp.route('/', methods=['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        data = "hello world"
        return jsonify({'data': data})


@bp.route('/live', methods=['POST'])
def add_ingredient():
    base64_img = ""
    try:
        if request.headers["Content-Type"] == "image/jpeg":
            base64_img = request.get_data()
    except Exception as e:
        return f"Unable to add ingredient. Exception: {e}"
    ingredient = Ingredient(name='test', picture=base64_img)
    ingredient.switch_collection('ingredients')
    ingredient.save()
    
    return jsonify({'data': "success"})


@bp.route("/ingredient/edit", methods=["POST"])
def edit_ingredient():
    id = request.form.get('id')
    ingredient = Ingredient.objects.get(id=id)

    for field in request.form:
        if field != 'id' and field in Ingredient._fields: # not O(1)
            ingredient[field] = request.form[field]

    ingredient.save()

    return jsonify({'data': f"ingredient with id {id} successfully updated"})


@bp.route("/ingredient/delete", methods=["DELETE"])
def delete_ingredient():
    id = request.form.get('id')
    ingredient = Ingredient.objects.get(id=id)
    ingredient.delete()
    return jsonify({'data': f"ingredient with id {id} successfully removed"})


@bp.route("/recipe/generate", methods=["GET"])
def generate_recipe():
    ingreds = []
    if request.args.get('use-all-ingreds', type=lambda v: v.lower() == 'true'):
        ingreds = Ingredient.objects
    else:
        ids = request.args.get('ids').split(",")
        ingreds = Ingredient.objects(id__in=ids)

    return jsonify({'data': f"ingredient with id {id} successfully removed"})
