from abc import ABC, abstractmethod


class ImageProcessor(ABC):

    @abstractmethod
    def execute(self, path: str, filenames: list | None = None):
        pass
