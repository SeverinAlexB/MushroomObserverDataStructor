import unittest
from Synonyms import SynonymManager


class TestStringMethods(unittest.TestCase):

    def load_data_test(self):
        manager = SynonymManager(limit=10)
        manager.load_data()
        self.assertIsNotNone(manager.synonyms)
        self.assertEqual(len(manager.synonyms), 10)

    def by_consensus_name_id_test(self):
        manager = SynonymManager()
        manager.load_data()
        result = manager.by_consensus_name_id(209)
        self.assertEqual(result.text_name, "Inocybe")

    def by_synonym_id_test(self):
        manager = SynonymManager()
        manager.load_data()
        result = manager.by_synonym_id(5180)
        self.assertEqual(len(result), 4)

    def by_get_item_test(self):
        manager = SynonymManager()
        manager.load_data()
        result = manager[343]
        for s in result:
            print(s)
        self.assertEqual(len(result), 3)

    def by_get_item_invalid_key_test(self):
        manager = SynonymManager()
        manager.load_data()
        result = manager[-1]
        self.assertEqual(len(result), 0)

