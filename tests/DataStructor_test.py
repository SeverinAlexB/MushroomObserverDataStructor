import unittest

from DataStructor import DataStructor
from ObserImages import ImageManager
from os.path import join, exists
from os import rmdir
from shutil import rmtree

class TestDataStructor(unittest.TestCase):

    def get_sample_obimage(self):
        manager = ImageManager(limit=10000)
        manager.load_data()
        obimage = manager.by_consensus_name_id(1104)
        return obimage

    def create_folder_test(self):
        obimage = self.get_sample_obimage()

        structor = DataStructor()
        structor._create_folder(obimage)
        new_folder = join(structor._folder_dataset, obimage.consensus_name)
        self.assertTrue(exists(new_folder))
        rmdir(new_folder)

    def create_folder_dict_test(self):
        obimage = self.get_sample_obimage()
        structor = DataStructor()
        structor._create_folder(obimage)

        folder_name = structor._get_folder_name(obimage.consensus_name)
        self.assertEqual(folder_name, obimage.consensus_name)

        new_folder = join(structor._folder_dataset, obimage.consensus_name)
        rmdir(new_folder)

    def create_folder_dict_synonym_test(self):
        obimage = self.get_sample_obimage()
        structor = DataStructor()
        structor._create_folder(obimage)

        folder_name = structor._get_folder_name(obimage.synonyms[0].text_name)
        self.assertEqual(folder_name, obimage.consensus_name)

        new_folder = join(structor._folder_dataset, obimage.consensus_name)
        rmdir(new_folder)

    def _image_path_a_test(self):
        structor = DataStructor()
        id = 7
        path = structor._image_path(id)
        print(path)
        self.assertTrue(exists(path))

    def _image_path_b_test(self):
        structor = DataStructor()
        id = 164042
        path = structor._image_path(id)
        print(path)
        self.assertTrue(exists(path))

    def struct_test(self):
        obimage = self.get_sample_obimage()
        structor = DataStructor()
        structor.struct(obimage)

        new_folder = join(structor._folder_dataset, obimage.consensus_name)
        rmtree(new_folder)







