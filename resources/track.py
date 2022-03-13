from flask_restful import Resource

from models.track import TrackModel


class TrackList(Resource):
    def get(self):
        track = TrackModel.find_all_tracks()
        if track is not None:
            return track
        else:
            return {'message': 'No track found'}, 404


class Track(Resource):
    def get(self, collection):
        track = TrackModel.find_by_collection(collection)
        if track is not None:
            return track
        else:
            return {'message': 'No track of the collection found'}, 404

