from flask_restful import Resource

from models.collection import CollectionModel


class CollectionList(Resource):
    def get(self):
        collection = CollectionModel.find_all_collections()
        if collection is not None:
            return collection
        else:
            return {'message': 'No collection found'}, 404


class Collection(Resource):
    def get(self, artist):
        collection = CollectionModel.find_by_artist(artist)
        if collection is not None:
            return collection
        else:
            return {'message': 'No collection of the artist found'}, 404

