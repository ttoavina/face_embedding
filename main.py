from logic.face_detector import face_detector
from logic.face_distance import face_distance
from services.model_singleton import ModelSingleton

if __name__ == "__main__":
    ModelSingleton.get_instance("./facenet_keras_weights.h5")

    print(face_distance("./faces/bean/bean4.jpg", "./faces/howard/howard1.jpg"))
