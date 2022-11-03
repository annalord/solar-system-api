from app.models.planet import Planet 

def test_get_all_planets_with_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [] 

def test_get_one_planet_returns_correct_planet(client, one_saved_planet):
    response = client.get("/planets/1")
    response_body = response.get_json() 

    assert response.status_code == 200 
    assert response_body["id"] == one_saved_planet.id
    assert response_body["name"] == one_saved_planet.name
    assert response_body["description"] == one_saved_planet.description
    assert response_body["type"] == one_saved_planet.type

def test_get_one_planet_with_no_records(client):
    response = client.get("/planets/1")
    response_body = response.get_json() 
    print(response_body)

    assert response.status_code == 404
    assert response_body == {"message" : "Planet 1 not found"}

def test_get_all_planets_with_one_record(client, one_saved_planet):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == [{
        "id" : 1, 
        "name" : "Earth",
        "description" : "has land and oceans",
        "type" : "Rocky"
    }]

def test_create_planet_happy_path(client):
    EXPECTED_PLANET = {
        "name": "Jupiter",
        "description": "huge and has storms",
        "type": "gas"
    }

    response = client.post("/planets", json=EXPECTED_PLANET)
    response_body = response.get_data(as_text=True)
    actual_planet = Planet.query.get(1)

    # assert
    assert response.status_code == 201
    assert response_body == f"New planet {EXPECTED_PLANET['name']} successfully created"
    assert actual_planet.name == EXPECTED_PLANET["name"]
    assert actual_planet.description == EXPECTED_PLANET["description"]
    assert actual_planet.type == EXPECTED_PLANET["type"]