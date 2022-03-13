from flask import Flask
from flask_restful import Api

from resources.artist import Artist
from resources.collection import CollectionList, Collection
from resources.track import TrackList, Track

app = Flask(__name__)
api = Api(app)


api.add_resource(Artist, "/artists")
api.add_resource(Collection, "/collection/<string:artist>")
api.add_resource(CollectionList, "/collections")
api.add_resource(Track, "/track/<string:collection>")
api.add_resource(TrackList, "/tracks")


if __name__ == "__main__":
    app.run(debug=True)
