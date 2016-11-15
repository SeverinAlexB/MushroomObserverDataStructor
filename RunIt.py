from ObserImages import ImageManager
from DataStructor import DataStructor
import datetime

structor = DataStructor()

manager = ImageManager()
manager.load_data()
images_count = len(manager.images)

counter = 0
for image in manager.images:
    structor.struct(image)

    if counter % 1000 == 0:
        print(str(datetime.datetime.now()) + ": " + str(counter) + "/" + str(images_count))
    counter += 1
