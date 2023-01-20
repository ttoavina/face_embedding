from utils.distance import eucludian_distance

from logic.face_detector import face_detector


def face_distance(image1_path, image2_path):
    f1 = face_detector(image1_path)
    f2 = face_detector(image2_path)

    dist = eucludian_distance(f1, f2)

    # sqrt((0-1)² *128) ~ 11.31
    return 1 - (dist / 11.31)
