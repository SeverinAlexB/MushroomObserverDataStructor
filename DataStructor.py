from ObserImages import ImageManager
from os.path import join, exists, basename
from os import mkdir
from shutil import copyfile


class DataStructor:
    def __init__(self):
        self._folder_a = '/home/severin/Downloads/320a/'
        self._folder_b = '/home/severin/Downloads/320b/'
        self._folder_dataset = '/home/severin/Downloads/mushroom_dataset/'
        self._names_to_folder = {}

    def _create_folder(self, obserimage):
        name = obserimage.consensus_name
        new_folder = join(self._folder_dataset, name)
        mkdir(new_folder)
        self._names_to_folder[name] = name
        for synonym in obserimage.synonyms:
            self._names_to_folder[synonym.text_name] = name

    def _get_folder_name(self, consensus_name):
        return self._names_to_folder[consensus_name]

    def _target_folder_exists(self, obserimage):
        return obserimage.consensus_name in self._names_to_folder

    def _image_path(self, image_id):
        path1 = join(self._folder_a, str(image_id) + ".jpg")
        path2 = join(self._folder_b, str(image_id) + ".jpg")
        if exists(path1):
            return path1
        elif exists(path2):
            return path2
        else:
            return ""

    def _copy_image(self, obserimage, folder_name):
        image_path = self._image_path(obserimage.image_id)
        file_name = basename(image_path)
        folder_path = join(self._folder_dataset, folder_name)
        target_path = join(folder_path, file_name)
        copyfile(image_path, target_path)

    def struct(self, obserimage):
        if not self._target_folder_exists(obserimage):
            self._create_folder(obserimage)
        folder_name = self._get_folder_name(obserimage.consensus_name)
        try:
            self._copy_image(obserimage, folder_name)
        except FileNotFoundError:
            print("\tImage not found. Image_id: " + str(obserimage.image_id) + ", name: " + obserimage.consensus_name)





