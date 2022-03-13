import psycopg2


class TrackModel:
    __table_name__ = "track"

    def __init__(self, track_id, collection_id, track_name, track_view_url, track_price, release_date, track_count,
                 track_number, track_time_millis):
        self.track_id = track_id
        self.collection_id = collection_id
        self.track_name = track_name
        self.track_view_url = track_view_url
        self.track_price = track_price
        self.release_date = release_date
        self.track_count = track_count
        self.track_number = track_number
        self.track_time_millis = track_time_millis

    @classmethod
    def find_all_tracks(cls):
        conn = psycopg2.connect(host='localhost',
                                database='python_pipeline',
                                user='postgres',
                                password='postgres',
                                port=5432)
        cur = conn.cursor()

        query = "SELECT * FROM track"
        cur.execute(query)
        rows = cur.fetchall()
        tracks = []
        for row in rows:
            tracks.append({
                'track_id': row[0],
                'collection_id': row[1],
                'track_name': row[2],
                'track_view_url': row[3],
                'track_price': row[4],
                'release_date': str(row[5]),
                'track_count': row[6],
                'track_number': row[7],
                'track_time_millis': row[8]
            })
        conn.close()

        return {'tracks': tracks}

    @classmethod
    def find_by_collection(cls, collection):
        conn = psycopg2.connect(host='localhost',
                                database='python_pipeline',
                                user='postgres',
                                password='postgres',
                                port=5432)
        cur = conn.cursor()

        query = "SELECT * FROM track t JOIN collection c ON c.collection_id = t.collection_id WHERE c.collection_name LIKE %s"
        cur.execute(query, (collection,))
        rows = cur.fetchall()
        tracks = []
        for row in rows:
            tracks.append({
                'track_id': row[0],
                'track_name': row[2],
                'track_view_url': row[3],
                'track_price': row[4],
                'release_date': str(row[5]),
                'track_count': row[6],
                'track_number': row[7],
                'track_time_millis': row[8]
            })
        conn.close()

        return {'tracks': tracks}


