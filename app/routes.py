from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, type):
        self.id = id
        self.name = name
        self.description = description
        self.type = type

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
        results_list.append(dict(
            id = planet.id,
            name = planet.name,
            description = planet.description,
            type = planet.type
        ))
    return jsonify(results_list)
