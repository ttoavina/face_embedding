import numpy as np
from PIL import Image
import tensorflow as tf

from services.model_singleton import ModelSingleton


def face_detector(image_path):
    model = ModelSingleton.get_instance()
    img = Image.open(image_path)
    resized_image = img.resize((160, 160))
    img_array = np.array(resized_image)
    return model.model.predict(tf.expand_dims(img_array, axis=0))[0]
