from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planet_bp = Blueprint("planets", __name__, url_prefix = "/planets")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"planet {planet_id} is invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message": f"planet {planet_id} not found"}, 404))
    
    return planet

@planet_bp.route("", methods = ["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],description=request_body["description"], type=request_body["type"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"New planet {new_planet.name} succesfully created", 201)

@planet_bp.route("", methods = ["GET"])
def read_all_planets():
    planets = Planet.query.all()
    planet_response = [planet.to_dict() for planet in planets]
    return jsonify(planet_response)

@planet_bp.route("/<id>", methods=["GET"])
def read_one_planet(id):
    planet = validate_planet(id)

    return jsonify(planet.to_dict()), 200

@planet_bp.route("/<id>", methods=["PUT"])
def update_planet(id):
    planet = validate_planet(id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.type = request_body["type"]

    db.session.commit()

    return make_response(f"Planet {planet.id} successfully updated"), 200

@planet_bp.route("/<id>", methods=["DELETE"])
def delete_planet(id):
    planet = validate_planet(id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet.id} successfully deleted"), 200