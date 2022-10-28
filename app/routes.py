from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request


planet_bp = Blueprint("planets", __name__, url_prefix = "/planets")

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

