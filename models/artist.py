import psycopg2


class ArtistModel:
    __table_name__ = "artist"

    def __init__(self, artist_id, artist_name, artist_view_url):
        self.artist_id = artist_id
        self.artist_name = artist_name
        self.artist_view_url = artist_view_url

    @classmethod
    def find_all_artist(cls):
        conn = psycopg2.connect(host='localhost',
                                database='python_pipeline',
                                user='postgres',
                                password='postgres',
                                port=5432)
        cur = conn.cursor()

        query = "SELECT * FROM artist"
        cur.execute(query)
        rows = cur.fetchall()
        artists = []
        for row in rows:
            artists.append({
                'artist_id': row[0],
                'artist_name': row[1],
                'artist_view_url': row[2]
            })
        conn.close()

        return {'artist': artists}


