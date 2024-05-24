from imageprocessor.imageprocessor import ImageProcessor


class Classifier:
    def __init__(
        self,
        processors: list[ImageProcessor] = None,
    ):

        self.processors = processors if processors else []

    def add_processor(self, processor: ImageProcessor) -> None:
        self.processors.append(processor)

    def get_classification(
        self,
        object_path: str,
    ) -> dict:

        classification = {}
        for proc in self.processors:
            result = proc.execute(object_path)
            print("!!!!")
            print(result)
            for avg, file_name in result:
                if file_name in classification:
                    classification[file_name] += float(avg)
                else:
                    classification[file_name] = float(avg)

        sorted(classification, key=lambda x: x[1])

        return classification


# beuty_classifier = Classifier()
# education_classifier = Classifier()
# relax_classifier = Classifier()
# restuarants_classifier = Classifier()
# dress_classifier = Classifier()

classifier_matrix = {
    key: Classifier()
    for key in ["beauty", "education", "relax", "restuarants", "dress"]
}
