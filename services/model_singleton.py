from keras.models import load_model

from utils.model_loader import ModelLoader


class ModelSingleton:
    instance = None

    @staticmethod
    def get_instance(path=None):
        if ModelSingleton.instance is None:
            if path is None: raise Exception("No model to create!")
            ModelSingleton.instance = ModelLoader(path)
            return ModelSingleton.instance

        return ModelSingleton.instance
