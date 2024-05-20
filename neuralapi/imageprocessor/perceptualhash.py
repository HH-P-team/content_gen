import os
from abc import ABC, abstractmethod

from PIL import Image
import imagehash
import distance


class ImageProcessor(ABC):

    @abstractmethod
    def eexecute(self, path: str, filenames: list | None = None):
        pass


class PerceptualHash(ImageProcessor):

    def __init__(self, dataset_path: str):
        self.dataset_path = dataset_path
        self.hashes = self._hash_map(dataset_path)

    def _hash_map(self, dataset_path: str) -> dict:
        hashes_map = {}
        file_names = os.listdir(dataset_path)
        for file_name in file_names:

            phash = str(
                imagehash.phash(
                    Image.open(dataset_path + f"/{file_name}"), 16
                )
            )
            if phash in hashes_map:
                hashes_map[phash].append(file_name)
            else:
                hashes_map[phash] = [file_name]

        return hashes_map

    def _distance_hash(self, q_image: Image, hashes: dict) -> list:
        h_distances = []

        query_image_phash = str(imagehash.phash(q_image, 16))
        for i_phash in hashes.keys():
            h_distances.append(
                {
                    "dist": distance.hamming(query_image_phash, i_phash),
                    "phash": i_phash,
                }
            )
        h_distances.sort(key=lambda item: item["dist"])
        h_distances = h_distances[:10]

        return h_distances

    def _avg_distance(self, distances):
        total = 0
        for item in distances:
            total += item["dist"]

        return total / len(distances)

    def execute(self, path: str, filenames: list | None = None) -> list:
        distance_img = []

        filenames = filenames if filenames else os.listdir(path)

        for file_name in filenames:

            query_image = Image.open(path + file_name)
            hamming_distances = self._distance_hash(query_image, self.hashes)
            avg = self._avg_distance(hamming_distances)
            distance_img.append((avg, file_name))

        distance_img.sort(key=lambda x: x[0])
        return distance_img
