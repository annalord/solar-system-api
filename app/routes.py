from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description, type):
        self.id = id
        self.name = name
        self.description = description
        self.type = type
    
    def to_json(self):
        return dict(
            id = self.id,
            name = self.name,
            description = self.description,
            type = self.type
        )   

planets = [
    Planet(1, "Mercury", "tan and small", "rocky"),
    Planet(2, "Venus", "hot and yellow", "rocky"),
    Planet(3, "Earth", "has land and oceans", "rocky"),
    Planet(4, "Mars", "red and dry", "rocky")
]

planet_bp = Blueprint("planets", __name__, url_prefix = "/planets")

@planet_bp.route("", methods = ["GET"])

def handle_planets():
    results_list = []
    for planet in planets:
        results_list.append(planet.to_json())
    return jsonify(results_list)

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"planet {planet_id} is invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message": f"planet {planet_id} not found"}, 404))

@planet_bp.route("/<id>", methods=["GET"])
def get_planet(id):
    planet = validate_planet(id)

    return jsonify(planet.to_json())