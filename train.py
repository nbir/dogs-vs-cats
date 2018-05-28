import glob

import cv2 as cv
import numpy as np

CLASS_NAMES = ['cat', 'dog']


def get_training_data():
    images = []
    labels = []

    for index, class_name in enumerate(CLASS_NAMES):
        filepaths = glob.glob('data/training/{}.*.jpg'.format(class_name))

        for filepath in filepaths:
            raw_image = cv.imread(filepath)
            resized_image = cv.resize(raw_image, (128, 128))
            float32_image = resized_image.astype(np.float32)
            normalized_image = np.multiply(float32_image, 1.0 / 255.0)

            images.append(normalized_image)
            labels.append(index)

    images = np.array(images)
    labels = np.array(labels)

    images, labels = shuffle(images, labels)

    return {'images': images, 'labels': labels}


def main():
    training_data = get_training_data()


if __name__ == '__main__':
    main()
