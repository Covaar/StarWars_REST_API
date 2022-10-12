from flask import Blueprint, jsonify, request
from models import Species

bpSpecies = Blueprint('bpSpecies', __name__)

@bpSpecies.route('/species', methods=['GET'])
def all_species():
    species = Species.query.all()
    species = list(map(lambda species: species.serialize(), species))
    return jsonify(species), 200

@bpSpecies.route('/species/<int:id>', methods=['GET'])
def get_species_by_id(id):
    species = Species.query.get(id)
    return jsonify(species.serialize()), 200