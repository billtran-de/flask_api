import psycopg2


class CollectionModel:
    __table_name__ = "collection"

    def __init__(self, collection_id, artist_id, collection_name, collection_view_url, collection_price, currency):
        self.collection_id = collection_id
        self.artist_id = artist_id
        self.collection_name = collection_name
        self.collection_view_url = collection_view_url
        self.collection_price = collection_price
        self.currency = currency

    @classmethod
    def find_all_collections(cls):
        conn = psycopg2.connect(host='localhost',
                                database='python_pipeline',
                                user='postgres',
                                password='postgres',
                                port=5432)
        cur = conn.cursor()

        query = "SELECT * FROM collection"
        cur.execute(query)
        rows = cur.fetchall()
        collections = []
        for row in rows:
            collections.append({
                'collection_id': row[0],
                'artist_id': row[1],
                'collection_name': row[2],
                'collection_view_url': row[3],
                'collection_price': str(row[4]) + " " + row[5]
            })
        conn.close()

        return {'collections': collections}

    @classmethod
    def find_by_artist(cls, artist):
        conn = psycopg2.connect(host='localhost',
                                database='python_pipeline',
                                user='postgres',
                                password='postgres',
                                port=5432)
        cur = conn.cursor()

        query = "SELECT * FROM collection c JOIN artist a ON c.artist_id = a.artist_id WHERE a.artist_name LIKE %s"
        cur.execute(query, (artist,))
        rows = cur.fetchall()
        collections = []
        for row in rows:
            collections.append({
                'collection_id': row[0],
                'collection_name': row[2],
                'collection_view_url': row[3],
                'collection_price': str(row[4]) + " " + row[5],
                'artist_name': row[7]
            })
        conn.close()

        return {'collections': collections}


