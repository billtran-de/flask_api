from flask_restful import Resource

from models.artist import ArtistModel


class Artist(Resource):
    def get(self):
        artist = ArtistModel.find_all_artist()
        if artist is not None:
            return artist
        else:
            return {'message': 'No artist found'},  404
