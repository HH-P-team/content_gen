from os import listdir
from os.path import splitext
import pickle as pk
from PIL import Image

import numpy as np
from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input
from sklearn.neighbors import NearestNeighbors

from imageprocessor.imageprocessor import ImageProcessor


class ResNet(ImageProcessor):

    def __init__(self, dataset_path: str):

        self.model = ResNet50(
            weights="imagenet",
            include_top=False,
            input_shape=(224, 224, 3),
            pooling="max",
        )
        self._generate_resnet_features(dataset_path)

    def _resize_img_to_array(self, img, img_shape):
        img_array = np.array(img.resize(img_shape, Image.LANCZOS))
        return img_array

    def _read_img_file(self, f):
        img = Image.open(f)
        if img.mode != "RGB":
            img = img.convert("RGB")
        return img

    def _get_features(self, img):
        img_width, img_height = 224, 224
        np_img = self._resize_img_to_array(
            img, img_shape=(img_width, img_height)
        )
        expanded_img_array = np.expand_dims(np_img, axis=0)
        preprocessed_img = preprocess_input(expanded_img_array)
        X_conv = self.model.predict(preprocessed_img)
        image_features = X_conv[0]
        image_features /= np.linalg.norm(image_features)
        return image_features

    def _generate_resnet_features(self, path):

        all_image_features = []
        image_filenames = listdir(path)
        image_ids = set(map(lambda el: splitext(el)[0], image_filenames))
        try:
            all_image_features = pk.load(
                open("resnet_image_features.pkl", "rb")
            )
        except (OSError, IOError) as e:
            print(f"file_not_found {e}")

        def exists_in_all_image_features(image_id):
            for image in all_image_features:
                if image["image_id"] == image_id:
                    # print("skipping "+ str(image_id))
                    return True
            return False

        def exists_in_image_folder(image_id):
            if image_id in image_ids:
                return True
            return False

        def sync_resnet_image_features():
            for_deletion = []
            for i in range(len(all_image_features)):
                if not exists_in_image_folder(
                    all_image_features[i]["image_id"]
                ):
                    print(
                        "deleting " + str(all_image_features[i]["image_id"])
                    )
                    for_deletion.append(i)
            for i in reversed(for_deletion):
                del all_image_features[i]

        sync_resnet_image_features()

        for image_filename in image_filenames:

            image_id = splitext(image_filename)[0]

            if exists_in_all_image_features(image_id):
                continue
            img_arr = self._read_img_file(path + "/" + image_filename)
            image_features = self._get_features(img_arr)

            # print(image_features)
            all_image_features.append(
                {"image_id": image_id, "features": image_features}
            )

        pk.dump(all_image_features, open("resnet_image_features.pkl", "wb"))

    def _found(self, query_image_features):
        image_features = pk.load(open("resnet_image_features.pkl", "rb"))
        features = []
        for image in image_features:
            features.append(np.array(image["features"]))
        features = np.array(features)
        features = np.squeeze(features)

        knn = NearestNeighbors(
            n_neighbors=20, algorithm="brute", metric="euclidean"
        )
        knn.fit(features)
        distances, indices = knn.kneighbors([query_image_features])

        return sum(distances[0]) / len(distances[0])

    def execute(self, path: str, filenames: list | None = None):

        # self._generate_resnet_features(dataset_path)

        weight_img = []

        for gen_image in listdir(path):
            query_image_pillow = Image.open(path + f"/{gen_image}").convert(
                "RGB"
            )
            query_image_features = self._get_features(query_image_pillow)
            distance = self._found(query_image_features)
            weight_img.append((distance, gen_image))

        weight_img.sort(key=lambda x: x[0])

        return weight_img
