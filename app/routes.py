from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planet_bp = Blueprint("planets", __name__, url_prefix = "/planets")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message": f"{cls.__name__} {model_id} is invalid"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message": f"{cls.__name__} {model_id} not found"}, 404))
    
    return model

@planet_bp.route("", methods = ["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"New planet {new_planet.name} successfully created", 201)

@planet_bp.route("", methods = ["GET"])
def read_all_planets():
    type_query = request.args.get("type")
    description_query = request.args.get("description")
    name_query = request.args.get("name")
    planet_query = Planet.query
    
    if name_query:
        planet_query = planet_query.filter_by(name=name_query)
    if description_query:
        planet_query = planet_query.filter_by(description=description_query)
    if type_query:
        planet_query = planet_query.filter_by(type=type_query)

    planets = planet_query.all()
    planet_response = [planet.to_dict() for planet in planets]
    return jsonify(planet_response)

@planet_bp.route("/<id>", methods=["GET"])
def read_one_planet(id):
    planet = validate_model(Planet, id)

    return jsonify(planet.to_dict()), 200

@planet_bp.route("/<id>", methods=["PUT"])
def update_planet(id):
    planet = validate_model(Planet, id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.type = request_body["type"]

    db.session.commit()

    return make_response(f"Planet {planet.id} successfully updated"), 200

@planet_bp.route("/<id>", methods=["DELETE"])
def delete_planet(id):
    planet = validate_model(Planet, id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet.id} successfully deleted"), 200