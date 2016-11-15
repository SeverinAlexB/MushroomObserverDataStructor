import psycopg2

from Synonyms import SynonymManager


class ObserImage:
    def __init__(self, observation_id, consensus_name_id, consensus_name, image_id):
        self._observation_id = observation_id
        self._consensus_name_id = consensus_name_id
        self._consensus_name = consensus_name
        self._image_id = image_id
        self._synonyms = []

    @property
    def observation_id(self):
        return self._observation_id

    @property
    def consensus_name_id(self):
        return self._consensus_name_id

    @property
    def consensus_name(self):
        return self._consensus_name

    @property
    def image_id(self):
        return self._image_id

    @property
    def synonyms(self):
        return self._synonyms

    def __str__(self):
        return (
            str(self.observation_id) + ", " + \
            str(self.consensus_name_id) + ", " + \
            str(self.consensus_name) + ", " + \
            str(self.image_id)
        )


class ImageManager:
    def __init__(self, limit=-1):
        self.connection_string = "dbname='mushroom' user='postgres' host='localhost' password='postgres'"
        self._images = []
        self._limit = limit
        self._synonym_manager = None

    @property
    def images(self):
        return self._images

    def _fetch_rows(self):
        conn = psycopg2.connect(self.connection_string)
        cur = conn.cursor()
        if self._limit == -1:
            cur.execute("""SELECT * from observation_images""")
        else:
            cur.execute("""SELECT * from observation_images limit """ + str(self._limit))

        rows = cur.fetchall()
        return rows

    def _load_synonym_manager(self):
        self._synonym_manager = SynonymManager()
        self._synonym_manager.load_data()

    def load_data(self):
        self._load_synonym_manager()
        rows = self._fetch_rows()
        for row in rows:
            observation_id, consensus_name_id, consensus_name, confidence, image_id = row
            obi = ObserImage(observation_id, consensus_name_id, consensus_name, image_id)
            obi._synonyms = self._synonym_manager[obi.consensus_name_id]
            self._images.append(obi)

    def by_consensus_name_id(self, key):
        for obimages in self._images:
            if obimages.consensus_name_id == key:
                return obimages
        return None
