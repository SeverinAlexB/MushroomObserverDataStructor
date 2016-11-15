import psycopg2

class Synonym:
    def __init__(self, consensus_name_id, synonym_id, text_name):
        self._consensus_name_id = consensus_name_id
        self._synonym_id = synonym_id
        self._text_name = text_name

    @property
    def text_name(self):
        return self._text_name

    @property
    def synonym_id(self):
        return self._synonym_id

    @property
    def consensus_name_id(self):
        return self._consensus_name_id

    def __str__(self):
        return str(self.consensus_name_id) + ", " + str(self.synonym_id) + ", " + self._text_name

class SynonymManager:
    def __init__(self, limit=-1):
        self.connection_string = "dbname='mushroom' user='postgres' host='localhost' password='postgres'"
        self._synonyms = []
        self._limit = limit
        self._synonms_consensus = {}
        self._synonms_id = {}

    @property
    def synonyms(self):
        return self._synonyms

    def __getitem__(self, key):
        '''
        Get all synonyms by consensus_name_id
        :param key: consensus_name_id
        :return: [Synonyms]
        '''
        synonym = self.by_consensus_name_id(key)
        if synonym is None:
            return []
        synonyms = self.by_synonym_id(synonym.synonym_id)
        result = []
        for s in synonyms:
            if not s.consensus_name_id == synonym.consensus_name_id:
                result.append(s)
        return result

    def by_consensus_name_id(self, key):
        try:
            return self._synonms_consensus[key]
        except KeyError:
            return None

    def by_synonym_id(self, key):
        try:
            return self._synonms_id[key]
        except KeyError:
            return []

    def _fetch_rows(self):
        conn = psycopg2.connect(self.connection_string)
        cur = conn.cursor()
        if self._limit == -1:
            cur.execute("""SELECT * from synonyms""")
        else:
            cur.execute("""SELECT * from synonyms limit """ + str(self._limit))

        rows = cur.fetchall()
        return rows

    def load_data(self):
        rows = self._fetch_rows()
        for row in rows:
            name_id, synonym_id, text_name = row
            s = Synonym(name_id, synonym_id, text_name)
            self._synonyms.append(s)

        for s in self._synonyms:
            self._synonms_consensus[s.consensus_name_id] = s
            if s.synonym_id not in self._synonms_id:
                self._synonms_id[s.synonym_id] = []
            self._synonms_id[s.synonym_id].append(s)


