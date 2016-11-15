import unittest

from ObserImages import ImageManager


class TestStringMethods(unittest.TestCase):
    def load_data_test(self):
        manager = ImageManager(limit=10)
        manager.load_data()
        self.assertIsNotNone(manager.images)
        self.assertEqual(len(manager.images), 10)

    def load_synonyms_test(self):
        manager = ImageManager(limit=10000)
        manager.load_data()
        obimage = manager.by_consensus_name_id(1104)
        for s in obimage.synonyms:
            print(s)
        self.assertEqual(len(obimage.synonyms), 2)

    def by_consensus_name_id_test(self):
        manager = ImageManager(limit=10)
        manager.load_data()
        obimage = manager.by_consensus_name_id(6)
        self.assertIsNotNone(obimage)
        self.assertEqual(obimage.consensus_name_id, 6)

