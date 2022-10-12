from flask import Blueprint, jsonify, request
from models import User, Planet, FavoritePlanet, FavoritePeople, People

bpFavorite = Blueprint('bpFavorite', __name__)

@bpFavorite.route('/favorite/planet/<int:planeta_id>', methods=['POST'])
def store_planet_by_user_id(planeta_id):
    new_favorite_planet = FavoritePlanet()
    new_favorite_planet.planet_id= planeta_id # ${planeta_id}
    new_favorite_planet.user_id = 1
    new_favorite_planet.save()
    
    return jsonify({"message":"Favorite Planet added"}), 200


@bpFavorite.route('/favorite/people/<int:p_id>', methods=['POST'])
def store_people_by_user_id(p_id):
    new_favorite_people = FavoritePeople()
    new_favorite_people.people_id= p_id # ${peoplea_id}
    new_favorite_people.user_id = 1
    new_favorite_people.save()
    
    return jsonify({"message":"Favorite People added"}), 200


@bpFavorite.route('/favorite/planet/<int:planeta_id>', methods=['DELETE'])
def delete_favorite_planet(planeta_id):
    delete_fav_planet = FavoritePlanet.query.filter_by(user_id=1,planet_id = planeta_id)
    delete_fav_planet.delete()
    
    return jsonify({"message":"Favorite Planet deleted"}), 200
 
@bpFavorite.route('/favorite/people/<int:p_id>', methods=['DELETE'])
def delete_favorite_people(p_id):
    delete_fav_people = FavoritePeople.query.filter_by(user_id=1,people_id = p_id)
    delete_fav_people.delete()
    
    return jsonify({"message":"Favorite People deleted"}), 200